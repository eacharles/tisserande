"""CECI stage node models — re-exported from nodes.py.

A CeciStageNode with execution_id=None is a schema-level stage definition
(python_path, version, default config).
A CeciStageNode with execution_id set is an instance-level record of a specific
stage execution, carrying per-run overrides.
"""

from .nodes import CeciStageNode, CeciStageNodeBase, CeciStageNodeCreate

__all__ = ["CeciStageNodeBase", "CeciStageNodeCreate", "CeciStageNode"]
