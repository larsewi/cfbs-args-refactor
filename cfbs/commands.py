"""
cfbs commands

Requirements:
 - These functions should not depend on each other.
"""


def init_command(
    name: str = None,
    description: str = None,
    index: str = None,
    masterfiles: bool = None,
    git: bool = None,
    git_user_name: str = None,
    git_user_email: str = None,
    non_interactive: bool = False,
) -> int:
    """
    Initialize a cfbs project.

    Parameters:
        name             (str): Specify project name.
        description      (str): Specify project description.
        index            (str): Specify index.
        masterfiles     (bool): Use default masterfiles policy framework.
        git             (bool): Use git source control engine.
        git_user_name    (str): Specify git user name.
        git_user_email   (str): Specify git user email.
        non_interactive (bool): Use default parameters instead of prompts.

    Returns:
        int: Exit code.
    """
    return 0


def status_command() -> int:
    """
    Print project status.

    Returns:
        int: Exit code.
    """
    return 0


def info_command(module: list[str], index: str = None) -> int:
    """
    Print module info.

    Parameters:
        module (str): Module name or alias.
        index  (str): Specify index.

    Returns:
        int: Exit code.
    """
    return 0


def search_command(module, index):
    return 0


def add_command(ctx):
    return 0


def remove_command(ctx):
    return 0


def clean_command(ctx):
    return 0


def update_command(ctx):
    return 0
