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

- **Nodes** — vertices in the DAG. A single `node` table with a `type_` discriminator column and nullable type-specific fields.
  - Data nodes: `data_file`, `config_file`, `config_dict`, `parameter`, `array`, `object`
  - Logic nodes: `python_function`, `member_function`, `shell_function`
- **Edges** — directed links between nodes (`from_id` → `to_id`)
  - Data → Logic = "input to function"
  - Logic → Data = "output from function"
- **Executions** — groups all nodes/edges from a single function call, with timing and status

Each node type can optionally reference a **type table** (e.g., `data_file_type`, `python_function`) for reusable definitions.

## Key Patterns

- **Single Node table**: All node types share one table with nullable columns. Simplifies graph queries since edges reference only one table.
- **UUID7 primary keys** for nodes/executions (time-ordered, via `uuid_utils`), int PKs for type tables and edges. Note: `uuid_utils.UUID` is not a subclass of `uuid.UUID` — we use a `_uuid7()` wrapper that returns standard `uuid.UUID`.
- **Macon integration**: Inherits `macon.db.base.Base`, uses `TableOperations`, `LocalOperations`, `SyncOperations`, `create_table_router`, `make_table_group`.
- **Three-model pattern** (from macon): `FooBase` → `FooCreate` (creation fields) → `Foo` (response with `id_`, `ConfigDict(from_attributes=True)`, `col_names_for_table`).
- **Tracking annotations**: `Annotated[]` type aliases (`DataFile[T]`, `Param[T]`, etc.) control how arguments are classified.
- **Pluggable backends**: `TrackingBackend` protocol allows `LocalSyncBackend` (real DB), `NullBackend` (testing), or custom implementations.
- **Decorator no-op**: If `configure()` hasn't been called, `@track` is transparent (function runs without tracking overhead).

## Critical Files

### Tracking system
- `src/tisserande/tracking/decorator.py` — `@track`, `@track_async`, `track_shell()`
- `src/tisserande/tracking/context.py` — `TrackingContext` orchestrates one execution lifecycle
- `src/tisserande/tracking/inspector.py` — `ArgumentInspector` classifies args → NodeType
- `src/tisserande/tracking/annotations.py` — `DataFile`, `Param`, `Untracked`, etc.
- `src/tisserande/tracking/backends.py` — `TrackingBackend` protocol, `LocalSyncBackend`, `NullBackend`

### Models & DB
- `src/tisserande/models/types.py` — `NodeType` and `ExecutionStatus` enums
- `src/tisserande/models/nodes.py` — All node Pydantic models (generic + typed variants)
- `src/tisserande/db/nodes.py` — Single `NodeTable` ORM model
- `src/tisserande/db/execution.py` — `ExecutionTable` ORM model
- `src/tisserande/db_oper/nodes.py` — `NodeOperations` with type-dependent FK resolution

### Configuration
- `src/tisserande/config.py` — `Configuration` class (env prefix: `TISSERANDE__`)

## Development

### Setup
```bash
pip install -e ".[dev]"
```

### Testing
```bash
pytest tests/                    # 28 tests, in-memory SQLite
pytest tests/ -x --tb=short     # stop at first failure
```

Tests use `sqlite+aiosqlite://` (in-memory). The `conftest.py` fixture calls `init_db()` and creates all tables before each test.

Coverage exclusion patterns (in `pyproject.toml`):
- `"pragma: no cover"` — explicit exclusion
- `"unexpected"` — unexpected-condition guards
- `"raise AssertionError"` / `"raise NotImplementedError"` — abstract/impossible paths

### Linting & Type Checking
```bash
ruff check src/ tests/
ruff format src/ tests/
mypy src/
```

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

### Dependencies
- Core: `macon[db]` (provides SQLAlchemy, pydantic, structlog, uuid_utils, anyio, aiosqlite, etc.)
- Optional: `numpy` (array support), `macon[server]` (FastAPI server), `macon[client]` (HTTP client)
- Docs: `sphinx`, `sphinx-autoapi`, `sphinx_rtd_theme`, `sphinx-autodoc-typehints`

### Adding a New Node Type

1. Add value to `NodeType` enum in `models/types.py`
2. Add nullable columns to `db/nodes.py` `NodeTable` if needed
3. Add FK mapping to `_TYPE_FK_MAP` in `db_oper/nodes.py`
4. Add typed Pydantic models (Base/Create/Response) in `models/nodes.py`
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
