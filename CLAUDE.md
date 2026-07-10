# CLAUDE.md — tisserande

## Overview

`tisserande` is a Python package for tracking execution provenance of Python functions and shell scripts. It records what functions were called, what data they consumed and produced, and how long they took — all as a directed acyclic graph (DAG) stored in a database.

The package builds on top of `macon` (at `/Users/echarles/software/KIPAC/macon`) which provides a layered CRUD framework. Tisserande adds tracking decorators for automatic provenance capture.

## Architecture — Layered Design

```
Tracking Decorators (@track, @track_async, track_shell)
  └── TrackingContext + ArgumentInspector
        └── TrackingBackend (LocalSyncBackend / NullBackend)
              └── local_sync (SyncOperations)  ← asyncio.run() wrappers
                    └── local_async (LocalOperations)  ← @with_session decorators
                          └── db_oper (TableOperations)  ← FK resolution
                                └── macon.db_funcs (raw async SQLAlchemy queries)
                                      └── macon.db (Base, session)
```

| Layer | Purpose | Key Base Class (from macon) |
|-------|---------|----------------------------|
| `models/` | Pydantic models (Base/Create/Response triplets) | `pydantic.BaseModel` |
| `db/` | SQLAlchemy ORM tables | `macon.db.base.Base` |
| `db_oper/` | `TableOperations` with FK resolution | `macon.db_oper.base.TableOperations` |
| `local_async/` | Session-managed async operations | `macon.local_async.base.LocalOperations` |
| `local_sync/` | Synchronous wrappers | `macon.local_sync.base.SyncOperations` |
| `tracking/` | Decorators, inspection, backends, context | *(tisserande-specific)* |
| `router/` | FastAPI app with auto-generated CRUD endpoints | `macon.router.base.create_table_router` |
| `cli/` | Click CLI entry points | `macon.cli.local.base.make_table_group` |
| `config.py` | Pydantic Settings configuration | `pydantic_settings.BaseSettings` |

## Domain Model

The provenance graph has three entity types:

- **Nodes** — vertices in the DAG. A base `node` table with a `type_` discriminator and per-type subtables via joined-table inheritance.
  - Data nodes: `data_file`, `config_file`, `config_dict`, `parameter`, `array`, `object`
  - Logic nodes: `python_function`, `member_function`, `shell_function`
- **Edges** — directed links between nodes (`from_id` → `to_id`)
  - Data → Logic = "input to function"
  - Logic → Data = "output from function"
- **Executions** — groups all nodes/edges from a single function call, with timing and status

Each node type can optionally reference a **type table** (e.g., `data_file_type`, `python_function`) for reusable definitions.

## Key Patterns

- **Joined-table inheritance**: A base `node` table holds shared columns (`id_`, `type_`, `execution_id`, `arg_name`); each node type has its own subtable (e.g., `data_file_node`, `parameter_node`) with type-specific columns. Edges FK to the base table, keeping graph queries simple.
- **UUID7 primary keys** for nodes/executions (time-ordered, via `uuid_utils`), int PKs for type tables and edges. Note: `uuid_utils.UUID` is not a subclass of `uuid.UUID` — we use a `uuid7()` wrapper in `db/utils.py` that returns standard `uuid.UUID`.
- **Macon integration**: Inherits `macon.db.base.Base`, uses `TableOperations`, `LocalOperations`, `SyncOperations`, `create_table_router`, `make_table_group`.
- **Three-model pattern** (from macon): `FooBase` → `FooCreate` (creation fields) → `Foo` (response with `id_`, `ConfigDict(from_attributes=True)`, `col_names_for_table`). Typed node models inherit from `_TypedNodeCreateMixin` and `_TypedNodeResponseMixin` to avoid repeating common fields (`arg_name`, `execution_id`, `id_`, `model_config`).
- **Tracking annotations**: `Annotated[]` type aliases (`DataFile[T]`, `Param[T]`, etc.) control how arguments are classified.
- **Pluggable backends**: `TrackingBackend` protocol allows `LocalSyncBackend` (real DB), `NullBackend` (testing), or custom implementations.
- **Decorator no-op**: If `configure()` hasn't been called, `@track` is transparent (function runs without tracking overhead).
- **Enum-based status/types**: Tracking code passes `ExecutionStatus` and `NodeType` enums; conversion to string values happens at the db_oper/backend layer.
- **`reset()`**: Clears the configured backend, making `configure()` safe to call multiple times (useful in tests).

## Critical Files

### Tracking system
- `src/tisserande/tracking/decorator.py` — `@track`, `@track_async`, `track_shell()`, `configure()`, `reset()`, `get_backend()`
- `src/tisserande/tracking/context.py` — `TrackingContext` orchestrates one execution lifecycle
- `src/tisserande/tracking/inspector.py` — `ArgumentInspector` classifies args → NodeType
- `src/tisserande/tracking/annotations.py` — `DataFile`, `Param`, `Untracked`, etc.
- `src/tisserande/tracking/backends.py` — `TrackingBackend` protocol, `LocalSyncBackend`, `NullBackend`

### Models & DB
- `src/tisserande/models/types.py` — `NodeType` and `ExecutionStatus` enums
- `src/tisserande/models/nodes.py` — All node Pydantic models (generic + typed variants)
- `src/tisserande/db/nodes.py` — `NodeTable` base + per-type subtables (joined-table inheritance)
- `src/tisserande/db/execution.py` — `ExecutionTable` ORM model
- `src/tisserande/db/utils.py` — Shared `uuid7()` helper for time-ordered primary keys
- `src/tisserande/db_oper/nodes.py` — `NodeOperations` with type-dependent FK resolution
- `src/tisserande/db_oper/execution.py` — `ExecutionOperations` with status enum conversion

### Configuration
- `src/tisserande/config.py` — `Configuration` class (env prefix: `TISSERANDE__`)

## Development

### Setup
```bash
pip install -e ".[dev]"
```

### Testing
```bash
pytest tests/                    # 86 tests, in-memory SQLite, 100% coverage
pytest tests/ -x --tb=short     # stop at first failure
pytest tests/ --cov=tisserande --cov-report=term-missing  # with coverage
```

Tests use `sqlite+aiosqlite://` (in-memory). The `conftest.py` fixture calls `init_db()` and creates all tables before each test.

Test files:
- `tests/test_tracking.py` — decorator and inspector unit tests with NullBackend
- `tests/test_full_stack.py` — end-to-end integration tests with real DB
- `tests/test_models.py` — Pydantic model validation
- `tests/test_inspector_coverage.py` — comprehensive inspector branch coverage
- `tests/test_decorator_coverage.py` — decorator flags and edge cases
- `tests/test_cli.py` — CLI entry points (Click test runner + mocked uvicorn)
- `tests/test_router.py` — FastAPI app creation and route registration
- `tests/test_db_oper_coverage.py` — FK resolution paths

Coverage exclusion patterns (in `pyproject.toml`):
- `"pragma: no cover"` — explicit exclusion
- `"unexpected"` — unexpected-condition guards
- `"raise AssertionError"` / `"raise NotImplementedError"` — abstract/impossible paths

### Linting & Type Checking
```bash
ruff check src/ tests/          # all checks pass
ruff format src/ tests/         # auto-format
mypy src/                       # no issues in 49 source files
pylint src/                     # 10.00/10
```

Ruff ignores: `COM812`, `N802-N816`, `UP047` (TypeVar over PEP 695 syntax).
Pylint disables: `C0415` (lazy imports), `W0603` (globals), `R0911` (many returns).

### Documentation
```bash
pip install -e ".[docs]"
cd docs && make html     # builds to docs/_build/html/
```
- Sphinx with `sphinx-autoapi` (API docs from source), `sphinx_rtd_theme`
- ReadTheDocs config: `.readthedocs.yaml`
- Docs source: `docs/` (index, getting_started, user_guide/, api/)

### Configuration
- `TISSERANDE__DB__URL` — database URL (default: `sqlite+aiosqlite:///tisserande.db`)
- `TISSERANDE__DB__ECHO` — SQLAlchemy echo (default: `false`)
- `TISSERANDE__TRACKING__ENABLED` — global enable/disable (default: `true`)
- `TISSERANDE__TRACKING__BACKEND` — default backend: `local_sync`, `null` (default: `local_sync`)
- `TISSERANDE__TRACKING__AUTO_CLASSIFY` — heuristic classification (default: `true`)
- Line length: 110 (ruff), 120 (pylint)
- Python: 3.13+ required
- Build: setuptools + setuptools_scm
- Package manager: pip (or uv)

### CLI Entry Points
- `tisserande-local` — local DB admin (CRUD for all tables via click)
- `tisserande-server` — FastAPI/uvicorn server

### CI/CD
GitHub Actions workflows in `.github/workflows/`:
- `linting.yml` — ruff + mypy on push/PR to main
- `testing-and-coverage.yml` — pytest on push/PR + weekly schedule
- `smoke-test.yml` — daily scheduled pytest run
- `docs.yml` — Sphinx build on docs/source changes
- `publish-to-pypi.yml` — trusted publishing on GitHub release

### Dependencies
- Core: `macon[db]` (provides SQLAlchemy, pydantic, structlog, uuid_utils, anyio, aiosqlite, etc.)
- Optional: `numpy` (array support), `macon[server]` (FastAPI server), `macon[client]` (HTTP client)
- Docs: `sphinx`, `sphinx-autoapi`, `sphinx_rtd_theme`, `sphinx-autodoc-typehints`

### Known Limitations
- **`@track_async` with `LocalSyncBackend`**: Cannot be used inside an already-running event loop because `LocalSyncBackend` internally calls `asyncio.run()` via macon's `local_sync`. A future `LocalAsyncBackend` would resolve this. For now, `@track_async` works when the decorated coroutine is called from synchronous code (e.g., `asyncio.run(my_func(...))`).

### Adding a New Node Type

1. Add value to `NodeType` enum in `models/types.py`
2. Add a subtable class in `db/nodes.py` inheriting from `NodeTable` (joined-table inheritance)
3. Add typed Pydantic models (Base/Create/Response) in `models/nodes.py` using `_TypedNodeCreateMixin` and `_TypedNodeResponseMixin`
4. Add FK mapping to `_TYPE_FK_MAP` and `_TYPE_DB_CLASS_MAP` in `db_oper/nodes.py`
5. Add heuristic classification in `tracking/inspector.py` `_classify_by_value()`
6. Add annotation alias in `tracking/annotations.py`

### Adding a New Type Table

1. Create Pydantic models (Base/Create/Response) in `models/data_types.py` or `models/function_types.py`
2. Create ORM table in `db/data_types.py` or `db/function_types.py`
3. Create `TableOperations` in `db_oper/`
4. Create `LocalOperations` in `local_async/`
5. Create `SyncOperations` in `local_sync/`
6. Add to `__init__.py` exports in each layer
7. Add router and CLI commands
