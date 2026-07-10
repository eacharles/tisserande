"""Tests for db_oper FK resolution paths."""

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
