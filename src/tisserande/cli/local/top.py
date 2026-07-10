import click
from macon.cli.local.base import make_table_group

from ...local_sync import (
    array,
    class_,
    config_dict_type,
    config_file_type,
    data_file_type,
    edge,
    execution,
    member_function,
    node,
    parameter,
    python_function,
    shell_function,
)


@click.group()
def cli() -> None:
    """Tisserande local database CLI."""


cli.add_command(make_table_group("data-file-type", data_file_type, "Manage data file types"))
cli.add_command(make_table_group("config-file-type", config_file_type, "Manage config file types"))
cli.add_command(make_table_group("config-dict-type", config_dict_type, "Manage config dict types"))
cli.add_command(make_table_group("parameter", parameter, "Manage parameters"))
cli.add_command(make_table_group("array", array, "Manage arrays"))
cli.add_command(make_table_group("class", class_, "Manage classes"))
cli.add_command(make_table_group("python-function", python_function, "Manage python functions"))
cli.add_command(make_table_group("member-function", member_function, "Manage member functions"))
cli.add_command(make_table_group("shell-function", shell_function, "Manage shell functions"))
cli.add_command(make_table_group("node", node, "Manage provenance nodes"))
cli.add_command(make_table_group("edge", edge, "Manage provenance edges"))
cli.add_command(make_table_group("execution", execution, "Manage executions"))
