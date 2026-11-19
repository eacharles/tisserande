"""Tests for Pydantic models."""

from tisserande.db.utils import uuid7
from tisserande.models import (
    DataFileCreate,
    DataFileType,
    DataFileTypeCreate,
    EdgeCreate,
    ParameterCreate,
    PythonFunction,
    PythonFunctionCreate,
)
from tisserande.models.types import ExecutionStatus, NodeType


class TestNodeType:
    def test_data_types(self):
        assert NodeType.DATA_FILE.is_data
        assert NodeType.CONFIG_FILE.is_data
        assert NodeType.PARAMETER.is_data
        assert not NodeType.PYTHON_FUNCTION_CALL.is_data

    def test_function_types(self):
        assert NodeType.PYTHON_FUNCTION_CALL.is_function
        assert NodeType.SHELL_FUNCTION_CALL.is_function
        assert not NodeType.DATA_FILE.is_function


class TestDataFileType:
    def test_create(self):
        obj = DataFileTypeCreate(name="fits", version="1.0")
        assert obj.name == "fits"

    def test_response(self):
        obj = DataFileType(id_=1, name="fits", version="1.0")
        assert obj.id_ == 1
        assert obj.name == "fits"


class TestPythonFunction:
    def test_create(self):
        obj = PythonFunctionCreate(name="process", module_="mymodule", version="1.0")
        assert obj.name == "process"
        assert obj.module_ == "mymodule"

    def test_response(self):
        obj = PythonFunction(id_=1, name="process", module_="mymodule", version="1.0")
        assert obj.id_ == 1


class TestTypedNodeCreate:
    def test_data_file_node(self):
        obj = DataFileCreate(file_path="/tmp/data.fits", creator="test")
        assert obj.node_type == NodeType.DATA_FILE
        assert obj.file_path == "/tmp/data.fits"

    def test_parameter_node(self):
        obj = ParameterCreate(value=3.14, creator="test")
        assert obj.node_type == NodeType.PARAMETER
        assert obj.value == 3.14


class TestEdge:
    def test_create(self):
        u1 = uuid7()
        u2 = uuid7()
        obj = EdgeCreate(from_id=u1, to_id=u2)
        assert obj.from_id == u1
        assert obj.to_id == u2


class TestExecutionStatus:
    def test_values(self):
        assert ExecutionStatus.PENDING.value == "pending"
        assert ExecutionStatus.RUNNING.value == "running"
        assert ExecutionStatus.SUCCESS.value == "success"
        assert ExecutionStatus.FAILURE.value == "failure"
