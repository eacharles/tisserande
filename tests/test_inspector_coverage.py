"""Additional tests for ArgumentInspector to cover remaining branches."""

import numpy as np

from tisserande.models.types import NodeType
from tisserande.tracking.annotations import ClassInstanceArg, ConfigFile, DataFile, Param, Untracked
from tisserande.tracking.inspector import ArgumentInspector, _classify_by_value


class TestClassifyByValue:
    def test_numpy_array(self):
        arr = np.array([1.0, 2.0, 3.0])
        assert _classify_by_value(arr) == NodeType.ARRAY

    def test_config_file_yaml(self):
        assert _classify_by_value("settings.yaml") == NodeType.CONFIG_FILE

    def test_config_file_json(self):
        assert _classify_by_value("config.json") == NodeType.CONFIG_FILE

    def test_config_file_toml(self):
        assert _classify_by_value("pyproject.toml") == NodeType.CONFIG_FILE

    def test_string_as_parameter(self):
        assert _classify_by_value("hello") == NodeType.PARAMETER

    def test_list_of_floats(self):
        assert _classify_by_value([1.0, 2.0, 3.0]) == NodeType.ARRAY

    def test_list_of_mixed(self):
        assert _classify_by_value([1.0, "two", 3.0]) == NodeType.CLASS_INSTANCE

    def test_empty_list(self):
        assert _classify_by_value([]) == NodeType.CLASS_INSTANCE

    def test_tuple_of_floats(self):
        assert _classify_by_value((1.0, 2.0)) == NodeType.ARRAY

    def test_custom_object(self):
        assert _classify_by_value(object()) == NodeType.CLASS_INSTANCE

    def test_boolean_not_parameter(self):
        assert _classify_by_value(True) == NodeType.CLASS_INSTANCE  # noqa: FBT003


class TestInspectorProperties:
    def test_function_name(self):
        def my_func(x: float) -> float:
            return x

        inspector = ArgumentInspector(my_func)
        assert inspector.function_name == "my_func"

    def test_function_module(self):
        def my_func(x: float) -> float:
            return x

        inspector = ArgumentInspector(my_func)
        assert inspector.function_module == __name__

    def test_hints_failure_graceful(self):
        """If get_type_hints fails, inspector still works with heuristics."""

        def broken_hints(x: "NonExistentType") -> float:  # noqa: F821
            return 0.0

        inspector = ArgumentInspector(broken_hints)
        assert inspector.classify_argument("x", 3.14) == NodeType.PARAMETER


class TestClassifyReturn:
    def test_classify_return_with_annotation(self):
        def fn(x: float) -> DataFile[str]:
            return "/tmp/out.fits"

        inspector = ArgumentInspector(fn)
        assert inspector.classify_return("/tmp/out.fits") == NodeType.DATA_FILE

    def test_classify_return_untracked(self):
        def fn(x: float) -> Untracked[str]:
            return "ignored"

        inspector = ArgumentInspector(fn)
        assert inspector.classify_return("ignored") is None

    def test_classify_return_no_annotation(self):
        def fn(x: float):
            return 42.0

        inspector = ArgumentInspector(fn)
        assert inspector.classify_return(42.0) == NodeType.PARAMETER


class TestBuildNodeKwargs:
    def test_config_file(self):
        def fn(cfg: ConfigFile[str]) -> None:
            pass

        inspector = ArgumentInspector(fn)
        result = inspector.build_node_kwargs(NodeType.CONFIG_FILE, "/etc/config.yaml")
        assert result["file_path"] == "/etc/config.yaml"
        assert result["node_type"] == NodeType.CONFIG_FILE

    def test_array(self):
        def fn(data: list) -> None:
            pass

        inspector = ArgumentInspector(fn)
        result = inspector.build_node_kwargs(NodeType.ARRAY, (1.0, 2.0, 3.0))
        assert result["shape"] == [3]

    def test_array_already_list(self):
        def fn(data: list) -> None:
            pass

        inspector = ArgumentInspector(fn)
        result = inspector.build_node_kwargs(NodeType.ARRAY, [1.0, 2.0])
        assert result["shape"] == [2]

    def test_class_instance(self):
        def fn(obj: ClassInstanceArg[dict]) -> None:
            pass

        inspector = ArgumentInspector(fn)
        result = inspector.build_node_kwargs(NodeType.CLASS_INSTANCE, {"key": "val"})
        assert result["node_type"] == NodeType.CLASS_INSTANCE
        assert "creator" in result

    def test_parameter_string_value(self):
        def fn(name: Param[str]) -> None:
            pass

        inspector = ArgumentInspector(fn)
        result = inspector.build_node_kwargs(NodeType.PARAMETER, "hello")
        assert result["value"] == 0.0

    def test_config_dict(self):
        def fn(cfg: dict) -> None:
            pass

        inspector = ArgumentInspector(fn)
        result = inspector.build_node_kwargs(NodeType.CONFIG_DICT, {"a": 1})
        assert result["config_data"] == {"a": 1}


class TestBuildInputSpecs:
    def test_skip_var_positional(self):
        def fn(*args: float) -> None:
            pass

        inspector = ArgumentInspector(fn)
        specs = inspector.build_input_specs((1.0, 2.0), {})
        assert len(specs) == 0

    def test_skip_var_keyword(self):
        def fn(**kwargs: float) -> None:
            pass

        inspector = ArgumentInspector(fn)
        specs = inspector.build_input_specs((), {"x": 1.0})
        assert len(specs) == 0

    def test_skip_untracked(self):
        def fn(x: Param[float], debug: Untracked[bool]) -> float:
            return x

        inspector = ArgumentInspector(fn)
        specs = inspector.build_input_specs((1.0, True), {})
        assert len(specs) == 1
        assert specs[0]["node_type"] == NodeType.PARAMETER


class TestBuildOutputSpecs:
    def test_none_result(self):
        def fn() -> None:
            pass

        inspector = ArgumentInspector(fn)
        assert inspector.build_output_specs(None) == []

    def test_untracked_return(self):
        def fn() -> Untracked[str]:
            return "ignored"

        inspector = ArgumentInspector(fn)
        assert inspector.build_output_specs("ignored") == []
