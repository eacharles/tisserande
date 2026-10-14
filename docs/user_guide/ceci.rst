CECI Pipeline Ingestion
=======================

Tisserande can import provenance records from `DESC CECI
<https://github.com/LSSTDESC/ceci>`_ pipelines. Two functions in
:mod:`tisserande.ceci_ingest` cover the full workflow:

1. :func:`~tisserande.ceci_ingest.register_pipeline_from_yaml` — read a CECI
   pipeline YAML file and create *schema-level* stage node records (one per
   unique stage class).
2. :func:`~tisserande.ceci_ingest.ingest_stage_logs` — read a directory of
   ``*.out`` log files produced by a CECI run and create execution, node, and
   edge records for the full pipeline and each individual stage.

Schema vs Instance Nodes
------------------------

Tisserande distinguishes two roles for every node type:

- **Schema node** (``execution_id=None``) — represents a class or file type
  *definition*, independent of any specific run.  Created by
  ``register_pipeline_from_yaml``.
- **Instance node** (``execution_id`` set) — represents a concrete object from a
  specific run.  Created by ``ingest_stage_logs``.

Both live in the same database table.  Instance stage nodes carry a
``ceci_stage_schema_node_id`` FK pointing back to their schema node, and instance
file nodes carry ``ceci_file_schema_node_id`` for the same purpose.

Quick Start
-----------

.. code-block:: python

   from tisserande.tracking import configure
   from tisserande.ceci_ingest import register_pipeline_from_yaml, ingest_stage_logs

   configure(db_url="sqlite+aiosqlite:///provenance.db")

   # 1. Register the pipeline definition (schema nodes)
   pipeline_create, schema_nodes = register_pipeline_from_yaml(
       "pz_dp1_6band.yaml",
       description="DESC DR1 photo-z 6-band pipeline",
   )

   # 2. Ingest a run's log files (instance nodes + edges)
   pipeline_exec, stage_results = ingest_stage_logs(
       "logs/",
       schema_nodes=schema_nodes,
   )

   print(f"Pipeline status : {pipeline_exec.status}")
   print(f"Duration        : {pipeline_exec.duration_seconds:.1f}s")
   print(f"Stages ingested : {len(stage_results)}")

   for exec_, stage_node, file_nodes in stage_results:
       n_in  = sum(1 for fn in file_nodes if not fn.arg_name == "output")
       n_out = sum(1 for fn in file_nodes if fn.arg_name == "output")
       print(f"  {stage_node.name}: {exec_.status}  "
             f"({n_in} inputs, {n_out} outputs)")

register_pipeline_from_yaml
----------------------------

.. code-block:: python

   from tisserande.ceci_ingest import register_pipeline_from_yaml

   pipeline_create, stage_nodes = register_pipeline_from_yaml(
       "pz_dp1_6band.yaml",
       name="pz_dp1_6band",        # defaults to YAML file stem
       description="6-band photo-z",
       config={},                  # optional default config dict
   )

**What it does:**

- Parses the YAML ``stages:`` list.
- Deduplicates stage entries by ``{module_name}.{classname}`` (the same class
  may appear many times in a pipeline under different instance names).
- Creates one :class:`~tisserande.models.nodes.CeciStageNode` schema node per
  unique stage class and writes it to the database.
- Returns a :class:`~tisserande.models.ceci_pipelines.CeciPipelineCreate` object
  (not yet persisted — the ``ceci_pipeline`` table infrastructure is ready if you
  want to persist it) and the list of created stage nodes.

ingest_stage_logs
-----------------

.. code-block:: python

   from tisserande.ceci_ingest import ingest_stage_logs

   pipeline_exec, stage_results = ingest_stage_logs(
       "logs/",
       schema_nodes=schema_nodes,   # optional, links instance → schema nodes
   )

**What it does:**

For each ``{stage_name}.out`` file found in ``log_dir``:

- Parses the ``Executing stage:`` line for class name and start timestamp.
- Parses the ``Stage complete:`` or ``Stage failed:`` line for end timestamp,
  duration, and status.
- Parses every ``Inserting handle into data store.`` line to collect file handles.
  Output files are identified by an ``inprogress_`` prefix in the filename (CECI
  convention); the prefix is stripped to give the final path.

After parsing all log files:

- Creates one **pipeline-level** :class:`~tisserande.models.execution.Execution`
  record whose ``start_time`` / ``end_time`` span the earliest and latest stage
  timestamps.  Status is ``failure`` if any stage failed, ``success`` otherwise.
- For each stage, creates a **stage-level** ``Execution`` (with
  ``parent_execution_id`` pointing to the pipeline execution), a
  :class:`~tisserande.models.nodes.CeciStageNode` instance, one
  :class:`~tisserande.models.nodes.CeciFileNode` instance per file handle, and
  the corresponding :class:`~tisserande.models.edges.Edge` records:

  - file → stage for input files
  - stage → file for output files

Returns ``(pipeline_execution, [(stage_exec, stage_node, [file_nodes]), ...])``.

Log File Format
---------------

Tisserande recognises three line patterns in CECI ``*.out`` log files:

.. code-block:: text

   Executing stage: FlexZBoostEstimator @ 2025-07-20 15:21:23.242275
   Inserting handle into data store.  model: /pz/data/model.pkl, estimate_fzboost
   Inserting handle into data store.  output: /pz/data/inprogress_output.hdf5, estimate_fzboost
   Stage complete: FlexZBoostEstimator @ 2025-07-20 15:21:25.913904 took 0.04 minutes

Or for a failed stage:

.. code-block:: text

   Executing stage: LephareInformer @ 2025-07-20 14:25:25.676534
   Inserting handle into data store.  input: /pz/data/train.hdf5, inform_lephare
   Stage failed: LephareInformer @ 2025-07-20 14:25:25.689365 after 0.00 minutes

The field immediately before the filename on a handle line (e.g. ``model``,
``input``, ``output``) is stored as ``arg_name`` on the file node.

Querying CECI Provenance
------------------------

After ingestion, use the standard layered operations to query the results:

.. code-block:: python

   from tisserande.local_sync import execution, node, edge
   from macon.models import Filter, FilterOp

   # Get the pipeline execution
   all_execs = execution.get_rows()
   pipeline_exec = next(e for e in all_execs if e.parent_execution_id is None)

   # Get all stage executions for this pipeline run
   stage_execs = execution.filter_rows(
       filters=[Filter(field="parent_execution_id", op=FilterOp.EQ,
                       value=str(pipeline_exec.id_))]
   )

   # Get all CECI stage nodes (instance level)
   ceci_stages = node.filter_rows(
       filters=[Filter(field="type_", op=FilterOp.EQ, value="ceci_stage"),
                Filter(field="execution_id", op=FilterOp.NE, value="null")]
   )

   # Get all file nodes produced by a specific stage
   for stage_node in ceci_stages:
       outgoing = edge.filter_rows(
           filters=[Filter(field="from_id", op=FilterOp.EQ, value=str(stage_node.id_))]
       )
       for e in outgoing:
           file_node = node.get_row(e.to_id)
           print(f"  {stage_node.name} → {file_node.path} (tag: {file_node.arg_name})")

CECI Pipeline Tables
--------------------

Beyond the node/edge/execution graph, tisserande provides dedicated schema tables
for CECI pipeline metadata:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Table accessor
     - Description
   * - ``ceci_pipeline``
     - Pipeline definition: name, YAML structure, default config
   * - ``ceci_pipeline_variant``
     - A named set of config overrides on a base pipeline
   * - ``ceci_pipeline_instance``
     - A specific pipeline run: date, status, and variant FK
   * - ``ceci_pipeline_stage_assoc``
     - Many-to-many link between a pipeline and its schema stage nodes

These are accessible via the same CRUD interface as all other tables:

.. code-block:: python

   from tisserande.local_sync import ceci_pipeline, ceci_pipeline_variant

   # List all registered pipelines
   for p in ceci_pipeline.get_rows():
       print(p.id_, p.name)

   # Create a variant
   variant = ceci_pipeline_variant.create_row(
       name="gold-sample",
       extra_description="Photo-z run on the gold galaxy sample",
       overrides={"njobs": 4},
       ceci_pipeline_id=pipeline_id,
   )
