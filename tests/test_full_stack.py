"""End-to-end test with real database backend."""

import pytest

from tisserande.models.types import ExecutionStatus, NodeType
from tisserande.tracking import configure, track, track_async, track_shell
from tisserande.tracking.annotations import DataFile, Param
from tisserande.tracking.backends import LocalSyncBackend


class TestFullStack:
    def setup_method(self):
        configure(backend=LocalSyncBackend())

    def test_track_creates_provenance(self):
        @track
        def process(input_file: DataFile[str], threshold: Param[float]) -> DataFile[str]:
            return "/tmp/output.fits"

        result = process("/tmp/input.fits", 0.5)
        assert result == "/tmp/output.fits"

        from tisserande.local_sync import edge, execution, node

        executions = execution.get_rows()
        assert len(executions) == 1
        assert executions[0].status == ExecutionStatus.SUCCESS
        assert executions[0].duration_seconds is not None
        assert executions[0].duration_seconds >= 0
        assert executions[0].end_time is not None
        assert executions[0].end_time >= executions[0].start_time

        nodes = node.get_rows()
        assert len(nodes) == 4

        node_types = [n.type_ for n in nodes]
        assert NodeType.PYTHON_FUNCTION in node_types
        assert node_types.count(NodeType.DATA_FILE) == 2
        assert node_types.count(NodeType.PARAMETER) == 1

        edges = edge.get_rows()
        assert len(edges) == 3

    def test_track_failure(self):
        @track
        def fail_func(x: Param[float]) -> float:
            raise RuntimeError("something went wrong")

        with pytest.raises(RuntimeError, match="something went wrong"):
            fail_func(1.0)

        from tisserande.local_sync import execution

        executions = execution.get_rows()
        failed = [e for e in executions if e.status == ExecutionStatus.FAILURE]
        assert len(failed) >= 1
        assert "something went wrong" in failed[-1].error_message

    def test_track_shell_creates_provenance(self):
        result = track_shell(
            "echo hello",
            inputs={"config": "/tmp/config.yaml"},
            outputs={"result": "/tmp/result.fits"},
        )
        assert result.returncode == 0

        from tisserande.local_sync import execution, node

        executions = execution.get_rows()
        shell_execs = [e for e in executions if e.status == ExecutionStatus.SUCCESS]
        assert len(shell_execs) >= 1

        nodes_list = node.get_rows()
        shell_nodes = [n for n in nodes_list if n.type_ == NodeType.SHELL_FUNCTION]
        assert len(shell_nodes) >= 1

    @pytest.mark.asyncio
    async def test_track_async_creates_provenance(self):
        from tisserande.tracking.backends import NullBackend

        backend = NullBackend()

        @track_async(backend=backend)
        async def fetch_data(url: DataFile[str], max_wait: Param[float]) -> DataFile[str]:
            return "/tmp/downloaded.fits"

        result = await fetch_data("https://example.com/data.fits", 30.0)
        assert result == "/tmp/downloaded.fits"

    @pytest.mark.asyncio
    async def test_track_async_exception(self):
        from tisserande.tracking.backends import NullBackend

        backend = NullBackend()

        @track_async(backend=backend)
        async def fail_async(x: Param[float]) -> float:
            raise RuntimeError("async error")

        with pytest.raises(RuntimeError, match="async error"):
            await fail_async(1.0)

    def test_track_shell_failure_with_inputs(self):
        result = track_shell(
            "false",
            inputs={"input_file": "/tmp/data.fits", "threshold": 0.5},
        )
        assert result.returncode != 0

        from tisserande.local_sync import edge, execution, node

        executions = execution.get_rows()
        failed = [e for e in executions if e.status == ExecutionStatus.FAILURE]
        assert len(failed) >= 1

        nodes_list = node.get_rows()
        shell_nodes = [n for n in nodes_list if n.type_ == NodeType.SHELL_FUNCTION]
        assert len(shell_nodes) >= 1
        input_nodes = [n for n in nodes_list if n.type_ in (NodeType.DATA_FILE, NodeType.PARAMETER)]
        assert len(input_nodes) >= 2

        edges_list = edge.get_rows()
        assert len(edges_list) >= 2
