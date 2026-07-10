import click
import uvicorn

from ...config import config


@click.command()
@click.option("--host", default="0.0.0.0", help="Host to bind to")
@click.option("--port", default=8080, type=int, help="Port to listen on")
@click.option("--reload/--no-reload", default=True, help="Enable auto-reload")
def serve(host: str, port: int, reload: bool) -> None:
    """Start the tisserande API server."""
    uvicorn.run(
        "tisserande.router.app:create_app",
        host=host,
        port=port,
        reload=reload,
        factory=True,
    )
