from fastapi import FastAPI
from macon.router.base import create_table_router

from ..local_async import (
    array,
    class_,
    config_dict_type,
    config_file_type,
    data_file_type,
    edge,
    execution,
    member_function,
    node,
    parameter,
    python_function,
    shell_function,
)


def create_app() -> FastAPI:
    """Create the tisserande FastAPI application."""
    app = FastAPI(title="tisserande", description="Execution provenance tracking API")

    app.include_router(create_table_router("data_file_type", data_file_type))
    app.include_router(create_table_router("config_file_type", config_file_type))
    app.include_router(create_table_router("config_dict_type", config_dict_type))
    app.include_router(create_table_router("parameter", parameter))
    app.include_router(create_table_router("array", array))
    app.include_router(create_table_router("class", class_))
    app.include_router(create_table_router("python_function", python_function))
    app.include_router(create_table_router("member_function", member_function))
    app.include_router(create_table_router("shell_function", shell_function))
    app.include_router(create_table_router("node", node))
    app.include_router(create_table_router("edge", edge))
    app.include_router(create_table_router("execution", execution))

    return app
