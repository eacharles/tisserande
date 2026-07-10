"""Tests for db_oper FK resolution paths."""

import pytest
from pydantic import ValidationError

from tisserande.db.nodes import (
    ArrayNodeTable,
    ConfigDictNodeTable,
    ConfigFileNodeTable,
    DataFileNodeTable,
    MemberFunctionNodeTable,
    ObjectNodeTable,
    ParameterNodeTable,
    PythonFunctionNodeTable,
    ShellFunctionNodeTable,
)
from tisserande.local_sync import (
    class_,
    data_file_type,
    member_function,
    node,
    python_function,
)
from tisserande.models.types import NodeType


class TestNodeOperationsFKResolution:
    def test_create_node_with_data_file_type_name(self):
        dft = data_file_type.create_row(name="FITS Image")
        assert dft.id_ is not None

        created = node.create_row(
            type_=NodeType.DATA_FILE.value,
            path="/tmp/image.fits",
            data_file_type_name="FITS Image",
        )
        assert created.data_file_type_id == dft.id_

    def test_create_node_with_python_function_name(self):
        pf = python_function.create_row(
            name="process_data",
            module_="mymodule",
        )
        assert pf.id_ is not None

        created = node.create_row(
            type_=NodeType.PYTHON_FUNCTION.value,
            python_function_name="process_data",
        )
        assert created.python_function_id == pf.id_


class TestMemberFunctionOperationsFKResolution:
    def test_create_member_function_with_class_name(self):
        cls = class_.create_row(name="MyClass", module_="mymodule")
        assert cls.id_ is not None

        mf = member_function.create_row(
            name="my_method",
            class_name="MyClass",
        )
        assert mf.class_id == cls.id_


class TestNodeTableClassmethods:
    @pytest.mark.parametrize(
        "table_cls,expected_string",
        [
            (DataFileNodeTable, "data_file_node"),
            (ConfigFileNodeTable, "config_file_node"),
            (ConfigDictNodeTable, "config_dict_node"),
            (ParameterNodeTable, "parameter_node"),
            (ArrayNodeTable, "array_node"),
            (ObjectNodeTable, "object_node"),
            (PythonFunctionNodeTable, "python_function_node"),
            (MemberFunctionNodeTable, "member_function_node"),
            (ShellFunctionNodeTable, "shell_function_node"),
        ],
    )
    def test_class_string(self, table_cls, expected_string):
        assert table_cls.class_string() == expected_string

    @pytest.mark.parametrize(
        "table_cls",
        [
            DataFileNodeTable,
            ConfigFileNodeTable,
            ConfigDictNodeTable,
            ParameterNodeTable,
            ArrayNodeTable,
            ObjectNodeTable,
            PythonFunctionNodeTable,
            MemberFunctionNodeTable,
            ShellFunctionNodeTable,
        ],
    )
    def test_pydantic_create_class(self, table_cls):
        cls = table_cls.pydantic_create_class()
        assert cls is not None
        assert hasattr(cls, "model_validate")

    @pytest.mark.parametrize(
        "table_cls",
        [
            DataFileNodeTable,
            ConfigFileNodeTable,
            ConfigDictNodeTable,
            ParameterNodeTable,
            ArrayNodeTable,
            ObjectNodeTable,
            PythonFunctionNodeTable,
            MemberFunctionNodeTable,
            ShellFunctionNodeTable,
        ],
    )
    def test_pydantic_model_class(self, table_cls):
        cls = table_cls.pydantic_model_class()
        assert cls is not None
        assert hasattr(cls, "model_validate")


class TestNodeCreateValidation:
    def test_create_node_validation_error_missing_required_field(self):
        with pytest.raises(ValidationError):
            node.create_row(type_=NodeType.DATA_FILE.value)
