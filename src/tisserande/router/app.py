from fastapi import FastAPI
from macon.router.base import create_table_router

from ..local_async import (
    array_type,
    assoc_template,
    association,
    class_type,
    config_dict_type,
    config_file_type,
    data_file_type,
    edge,
    edge_template,
    graph,
    graph_template,
    member_function,
    node,
    node_template,
    parameter_type,
    python_function,
    shell_function,
)


def create_app() -> FastAPI:
    """Create the tisserande FastAPI application."""
    app = FastAPI(title="tisserande", description="Execution provenance tracking API")

    # NodeTemplate base + data type templates
    app.include_router(create_table_router("node-template", node_template))
    app.include_router(create_table_router("data-file-type", data_file_type))
    app.include_router(create_table_router("config-file-type", config_file_type))
    app.include_router(create_table_router("config-dict-type", config_dict_type))
    app.include_router(create_table_router("parameter-type", parameter_type))
    app.include_router(create_table_router("array-type", array_type))
    app.include_router(create_table_router("class-type", class_type))

    # Function type templates
    app.include_router(create_table_router("python-function", python_function))
    app.include_router(create_table_router("member-function", member_function))
    app.include_router(create_table_router("shell-function", shell_function))

    # Graph templates + graphs
    app.include_router(create_table_router("graph-template", graph_template))
    app.include_router(create_table_router("graph", graph))

    # Node instances + edges
    app.include_router(create_table_router("node", node))
    app.include_router(create_table_router("edge-template", edge_template))
    app.include_router(create_table_router("edge", edge))

    # Associations
    app.include_router(create_table_router("assoc-template", assoc_template))
    app.include_router(create_table_router("association", association))

    return app
