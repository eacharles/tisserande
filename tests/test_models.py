"""Tests for Pydantic models."""

import uuid

from tisserande.models import (
    DataFileType,
    DataFileTypeCreate,
    EdgeCreate,
    ExecutionCreate,
    NodeCreate,
    PythonFunction,
    PythonFunctionCreate,
)
from tisserande.models.types import ExecutionStatus, NodeType


class TestNodeType:
    def test_data_types(self):
        assert NodeType.DATA_FILE.is_data
        assert NodeType.CONFIG_FILE.is_data
        assert NodeType.PARAMETER.is_data
        assert not NodeType.PYTHON_FUNCTION.is_data

    def test_logic_types(self):
        assert NodeType.PYTHON_FUNCTION.is_logic
        assert NodeType.SHELL_FUNCTION.is_logic
        assert not NodeType.DATA_FILE.is_logic


class TestDataFileType:
    def test_create(self):
        obj = DataFileTypeCreate(name="fits")
        assert obj.name == "fits"

    def test_response(self):
        obj = DataFileType(id_=1, name="fits")
        assert obj.id_ == 1
        assert obj.name == "fits"


class TestPythonFunction:
    def test_create(self):
        obj = PythonFunctionCreate(name="process", module_="mymodule")
        assert obj.name == "process"
        assert obj.module_ == "mymodule"

    def test_response(self):
        obj = PythonFunction(id_=1, name="process", module_="mymodule")
        assert obj.id_ == 1


class TestNodeCreate:
    def test_data_file_node(self):
        obj = NodeCreate(type_=NodeType.DATA_FILE, path="/tmp/data.fits")
        assert obj.type_ == NodeType.DATA_FILE
        assert obj.path == "/tmp/data.fits"

    def test_parameter_node(self):
        obj = NodeCreate(type_=NodeType.PARAMETER, value_float=3.14)
        assert obj.value_float == 3.14


class TestEdge:
    def test_create(self):
        u1 = uuid.uuid4()
        u2 = uuid.uuid4()
        obj = EdgeCreate(from_id=u1, to_id=u2)
        assert obj.from_id == u1
        assert obj.to_id == u2


class TestExecution:
    def test_create(self):
        obj = ExecutionCreate(status=ExecutionStatus.RUNNING)
        assert obj.status == ExecutionStatus.RUNNING

    def test_defaults(self):
        obj = ExecutionCreate()
        assert obj.status == ExecutionStatus.PENDING
