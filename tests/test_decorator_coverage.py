"""Additional tests for decorator.py to cover remaining branches."""

import pytest

from tisserande.tracking import configure, get_backend, reset, track, track_async, track_shell
from tisserande.tracking.backends import NullBackend


class TestConfigureResetGetBackend:
    def setup_method(self):
        reset()

    def teardown_method(self):
        reset()

    def test_get_backend_initially_none(self):
        assert get_backend() is None

    def test_configure_sets_backend(self):
        backend = NullBackend()
        configure(backend=backend)
        assert get_backend() is backend

    def test_reset_clears_backend(self):
        configure(backend=NullBackend())
        assert get_backend() is not None
        reset()
        assert get_backend() is None


class TestTrackNoBackend:
    def setup_method(self):
        reset()

    def teardown_method(self):
        reset()

    def test_track_no_backend_passthrough(self):
        @track
        def add(x: float, y: float) -> float:
            return x + y

        assert add(1.0, 2.0) == 3.0

    @pytest.mark.asyncio
    async def test_track_async_no_backend_passthrough(self):
        @track_async
        async def add(x: float, y: float) -> float:
            return x + y

        assert await add(1.0, 2.0) == 3.0

    def test_track_shell_no_backend_passthrough(self):
        result = track_shell("echo hello")
        assert result.returncode == 0
        assert "hello" in result.stdout


class TestTrackInputsOutputsFlags:
    def setup_method(self):
        self.backend = NullBackend()

    def test_track_inputs_false(self):
        @track(backend=self.backend, track_inputs=False)
        def add(x: float = 0.0, y: float = 0.0) -> float:
            return x + y

        assert add(1.0, 2.0) == 3.0

    def test_track_outputs_false(self):
        @track(backend=self.backend, track_outputs=False)
        def add(x: float, y: float) -> float:
            return x + y

        assert add(1.0, 2.0) == 3.0

    @pytest.mark.asyncio
    async def test_track_async_inputs_false(self):
        @track_async(backend=self.backend, track_inputs=False)
        async def add(x: float = 0.0, y: float = 0.0) -> float:
            return x + y

        assert await add(1.0, 2.0) == 3.0

    @pytest.mark.asyncio
    async def test_track_async_outputs_false(self):
        @track_async(backend=self.backend, track_outputs=False)
        async def add(x: float, y: float) -> float:
            return x + y

        assert await add(1.0, 2.0) == 3.0

    @pytest.mark.asyncio
    async def test_track_async_bare_decorator(self):
        configure(backend=self.backend)

        @track_async
        async def multiply(a: float, b: float) -> float:
            return a * b

        assert await multiply(3.0, 4.0) == 12.0
        reset()


class TestTrackShellOutputs:
    def setup_method(self):
        self.backend = NullBackend()

    def test_track_shell_with_outputs(self):
        result = track_shell(
            "echo done",
            outputs={"result_file": "/tmp/output.fits"},
            backend=self.backend,
        )
        assert result.returncode == 0

    def test_track_shell_with_dict_input(self):
        result = track_shell(
            "echo done",
            inputs={"config": {"key": "value"}},
            backend=self.backend,
        )
        assert result.returncode == 0

    def test_track_shell_with_object_input(self):
        result = track_shell(
            "echo done",
            inputs={"data": [1, "mixed", 3]},
            backend=self.backend,
        )
        assert result.returncode == 0

    def test_track_shell_with_list_command(self):
        result = track_shell(
            ["echo", "hello"],
            backend=self.backend,
        )
        assert result.returncode == 0

    def test_track_shell_with_config_dict_output(self):
        result = track_shell(
            "echo done",
            outputs={"config": {"out_key": "out_val"}},
            backend=self.backend,
        )
        assert result.returncode == 0

    def test_track_shell_with_parameter_output(self):
        result = track_shell(
            "echo done",
            outputs={"score": 0.95},
            backend=self.backend,
        )
        assert result.returncode == 0

    def test_track_shell_with_object_output(self):
        result = track_shell(
            "echo done",
            outputs={"misc": [1, "two", 3]},
            backend=self.backend,
        )
        assert result.returncode == 0
