"""Tests for the FastAPI router application."""

from tisserande.router.app import create_app


class TestCreateApp:
    def test_create_app_returns_fastapi(self):
        app = create_app()
        assert app.title == "tisserande"

    def test_create_app_has_routes(self):
        app = create_app()
        openapi = app.openapi()
        paths = list(openapi["paths"].keys())
        assert any("node" in p for p in paths)
        assert any("edge" in p for p in paths)
        assert any("execution" in p for p in paths)
        assert any("data_file_type" in p for p in paths)
        assert any("python_function" in p for p in paths)
