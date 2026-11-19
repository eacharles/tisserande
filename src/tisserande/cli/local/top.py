import click
from macon.cli.local.base import make_table_group

from ...local_sync import (
    array_type,
    assoc_template,
    association,
    class_type,
    config_dict_type,
    config_file_type,
    data_file_type,
    edge,
    edge_template,
    graph,
    graph_template,
    member_function,
    node,
    node_template,
    parameter_type,
    python_function,
    shell_function,
)


@click.group()
def cli() -> None:
    """Tisserande local database CLI."""


# NodeTemplate base + data type templates
cli.add_command(make_table_group("node-template", node_template, "Manage node templates"))
cli.add_command(make_table_group("data-file-type", data_file_type, "Manage data file types"))
cli.add_command(make_table_group("config-file-type", config_file_type, "Manage config file types"))
cli.add_command(make_table_group("config-dict-type", config_dict_type, "Manage config dict types"))
cli.add_command(make_table_group("parameter-type", parameter_type, "Manage parameter types"))
cli.add_command(make_table_group("array-type", array_type, "Manage array types"))
cli.add_command(make_table_group("class-type", class_type, "Manage Python class types"))

# Function type templates
cli.add_command(make_table_group("python-function", python_function, "Manage python functions"))
cli.add_command(make_table_group("member-function", member_function, "Manage member functions"))
cli.add_command(make_table_group("shell-function", shell_function, "Manage shell functions"))

# Graph templates + graphs
cli.add_command(make_table_group("graph-template", graph_template, "Manage graph templates"))
cli.add_command(make_table_group("graph", graph, "Manage graph executions"))

# Node instances + edges
cli.add_command(make_table_group("node", node, "Manage provenance nodes"))
cli.add_command(make_table_group("edge-template", edge_template, "Manage edge templates"))
cli.add_command(make_table_group("edge", edge, "Manage provenance edges"))

# Associations
cli.add_command(make_table_group("assoc-template", assoc_template, "Manage assoc templates"))
cli.add_command(make_table_group("association", association, "Manage node–graph associations"))
