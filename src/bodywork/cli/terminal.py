from typing import Any, Dict, Optional

from rich.console import Console
from rich.table import Table

console = Console(highlight=False, soft_wrap=False, force_terminal=True)


def print_info(msg: str) -> None:
    """Print an info message."""
    console.print(msg, style="green")


def print_warn(msg: str) -> None:
    """Print a warning message."""
    console.print(msg, style="red")


def print_dict(
    the_dict: Dict[str, Any],
    table_name: Optional[str] = None,
    key_col_name: str = "Field",
    val_col_name: str = "Value"
) -> None:
    """Render dict as a table in terminal.

    :param the_dict: The dictionary to render.
    :param table_name: Table name, defaults to None.
    :param key_col_name: Header for the keys column, defaults to 'Field'.
    :param val_col_name: Header for the values column, defaults to 'Value'.
    """
    table = Table(title=f"{table_name if table_name else ''}", title_style="bold")
    table.add_column(f"[yellow]{key_col_name}[/yellow]", style="bold purple")
    table.add_column(f"[yellow]{val_col_name}[/yellow]", style="bold green")
    for field, value in the_dict.items():
        table.add_row(str(field), str(value))
    console.print(table)


def print_pod_logs(logs: str, name: str) -> None:
    """Render pod lods.

    :param logs: The logs!
    :param name: The name of the pod associated with the logs.
    """
    console.rule(f"[yellow]logs {name} stage[/yellow]", style="yellow")
    console.print(logs, style="grey58")
    console.rule(style="yellow")


if __name__ == "__main__":
    s = "alex ioannides is the bomb " * 10
    console.print(s)
