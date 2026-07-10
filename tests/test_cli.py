"""Tests for CLI entry points."""

from unittest.mock import patch

from click.testing import CliRunner

from tisserande.cli.local.top import cli


class TestLocalCli:
    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Tisserande local database CLI" in result.output

    def test_cli_subcommands_exist(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert "node" in result.output
        assert "edge" in result.output
        assert "execution" in result.output
        assert "data-file-type" in result.output


class TestServerCli:
    def test_serve_help(self):
        from tisserande.cli.server.top import serve

        runner = CliRunner()
        result = runner.invoke(serve, ["--help"])
        assert result.exit_code == 0
        assert "--host" in result.output
        assert "--port" in result.output
        assert "--reload" in result.output

    @patch("tisserande.cli.server.top.uvicorn.run")
    def test_serve_invokes_uvicorn(self, mock_run):
        from tisserande.cli.server.top import serve

        runner = CliRunner()
        result = runner.invoke(serve, ["--host", "127.0.0.1", "--port", "9000", "--no-reload"])
        assert result.exit_code == 0
        mock_run.assert_called_once_with(
            "tisserande.router.app:create_app",
            host="127.0.0.1",
            port=9000,
            reload=False,
            factory=True,
        )
