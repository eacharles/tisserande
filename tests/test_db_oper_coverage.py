"""Tests for db_oper FK resolution paths."""

import pytest
from pydantic import ValidationError

from tisserande.db.nodes import (
    Array,
    ClassInstance,
    ConfigDict,
    ConfigFile,
    DataFile,
    MemberFunctionCall,
    Parameter,
    PythonFunctionCall,
    ShellFunctionCall,
)
from tisserande.local_sync import (
    class_type,
    data_file_type,
    member_function,
    node,
    python_function,
)
from tisserande.models.types import NodeType


class TestNodeOperationsFKResolution:
    def test_create_node_with_data_file_type_name(self):
        dft = data_file_type.create_row(name="FITS Image", version="1.0")
        assert dft.id_ is not None

        created = node.create_row(
            node_type=NodeType.DATA_FILE.value,
            file_path="/tmp/image.fits",
            creator="test",
            node_template_name="FITS Image",
        )
        assert created.node_template_id == dft.id_

    def test_create_node_with_python_function_name(self):
        pf = python_function.create_row(
            name="process_data",
            module_="mymodule",
            version="1.0",
        )
        assert pf.id_ is not None

        created = node.create_row(
            node_type=NodeType.PYTHON_FUNCTION_CALL.value,
            node_template_name="process_data",
        )
        assert created.node_template_id == pf.id_


class TestMemberFunctionOperationsFKResolution:
    def test_create_member_function_with_class_name(self):
        cls = class_type.create_row(name="MyClass", module_="mymodule", version="1.0")
        assert cls.id_ is not None

        mf = member_function.create_row(
            name="my_method",
            version="1.0",
            class_name="MyClass",
        )
        assert mf.class_id == cls.id_


class TestNodeTableClassmethods:
    @pytest.mark.parametrize(
        "table_cls,expected_string",
        [
            (DataFile, "data_file"),
            (ConfigFile, "config_file"),
            (ConfigDict, "config_dict"),
            (Parameter, "parameter"),
            (Array, "array"),
            (ClassInstance, "class_instance"),
            (PythonFunctionCall, "python_function_call"),
            (MemberFunctionCall, "member_function_call"),
            (ShellFunctionCall, "shell_function_call"),
        ],
    )
    def test_class_string(self, table_cls, expected_string):
        assert table_cls.class_string() == expected_string

    @pytest.mark.parametrize(
        "table_cls",
        [
            DataFile,
            ConfigFile,
            ConfigDict,
            Parameter,
            Array,
            ClassInstance,
            PythonFunctionCall,
            MemberFunctionCall,
            ShellFunctionCall,
        ],
    )
    def test_pydantic_create_class(self, table_cls):
        cls = table_cls.pydantic_create_class()
        assert cls is not None
        assert hasattr(cls, "model_validate")

    @pytest.mark.parametrize(
        "table_cls",
        [
            DataFile,
            ConfigFile,
            ConfigDict,
            Parameter,
            Array,
            ClassInstance,
            PythonFunctionCall,
            MemberFunctionCall,
            ShellFunctionCall,
        ],
    )
    def test_pydantic_model_class(self, table_cls):
        cls = table_cls.pydantic_model_class()
        assert cls is not None
        assert hasattr(cls, "model_validate")


class TestNodeCreateValidation:
    def test_create_node_validation_error_missing_required_field(self):
        with pytest.raises(ValidationError):
            node.create_row(node_type=NodeType.DATA_FILE.value)
