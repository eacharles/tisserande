"""Tests for the tracking decorator with NullBackend."""

from tisserande.tracking import configure, track, track_shell
from tisserande.tracking.annotations import DataFile, Param
from tisserande.tracking.backends import NullBackend
from tisserande.tracking.inspector import ArgumentInspector


class TestArgumentInspector:
    def test_classify_float(self):
        def fn(x: float) -> float:
            return x

        inspector = ArgumentInspector(fn)
        from tisserande.models.types import NodeType

        assert inspector.classify_argument("x", 3.14) == NodeType.PARAMETER

    def test_classify_path(self):
        def fn(path: str) -> str:
            return path

        inspector = ArgumentInspector(fn)
        from tisserande.models.types import NodeType

        assert inspector.classify_argument("path", "/tmp/data.fits") == NodeType.DATA_FILE

    def test_classify_dict(self):
        def fn(cfg: dict) -> None:
            pass

        inspector = ArgumentInspector(fn)
        from tisserande.models.types import NodeType

        assert inspector.classify_argument("cfg", {"key": "val"}) == NodeType.CONFIG_DICT

    def test_build_input_specs(self):
        def fn(x: float, y: float) -> float:
            return x + y

        inspector = ArgumentInspector(fn)
        specs = inspector.build_input_specs((1.0, 2.0), {})
        assert len(specs) == 2
        assert specs[0]["arg_name"] == "x"
        assert specs[1]["arg_name"] == "y"

    def test_build_output_specs(self):
        def fn() -> float:
            return 1.0

        inspector = ArgumentInspector(fn)
        specs = inspector.build_output_specs(42.0)
        assert len(specs) == 1
        assert specs[0]["arg_name"] == "return"

    def test_tuple_return(self):
        def fn() -> tuple:
            return (1.0, 2.0)

        inspector = ArgumentInspector(fn)
        specs = inspector.build_output_specs((1.0, 2.0))
        assert len(specs) == 2


class TestTrackDecorator:
    def setup_method(self):
        self.backend = NullBackend()

    def test_track_basic(self):
        @track(backend=self.backend)
        def add(x: float, y: float) -> float:
            return x + y

        result = add(1.0, 2.0)
        assert result == 3.0

    def test_track_no_args(self):
        @track(backend=self.backend)
        def hello() -> str:
            return "world"

        assert hello() == "world"

    def test_track_exception(self):
        @track(backend=self.backend)
        def fail() -> None:
            raise ValueError("test error")

        import pytest

        with pytest.raises(ValueError, match="test error"):
            fail()

    def test_track_bare_decorator(self):
        configure(backend=self.backend)

        @track
        def multiply(a: float, b: float) -> float:
            return a * b

        assert multiply(3.0, 4.0) == 12.0

    def test_track_with_annotations(self):
        @track(backend=self.backend)
        def process(input_file: DataFile[str], threshold: Param[float]) -> DataFile[str]:
            return "/tmp/output.fits"

        result = process("/tmp/input.fits", 0.5)
        assert result == "/tmp/output.fits"


class TestTrackShell:
    def setup_method(self):
        self.backend = NullBackend()

    def test_track_shell_success(self):
        result = track_shell("echo hello", backend=self.backend)
        assert result.returncode == 0
        assert "hello" in result.stdout

    def test_track_shell_with_inputs(self):
        result = track_shell(
            "echo test",
            inputs={"input_file": "/tmp/data.fits"},
            backend=self.backend,
        )
        assert result.returncode == 0

    def test_track_shell_failure(self):
        result = track_shell("false", backend=self.backend)
        assert result.returncode != 0
