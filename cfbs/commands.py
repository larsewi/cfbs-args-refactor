"""
cfbs commands

Requirements:
 - These functions should not directly or indirectly depend on each other.
 - This file should only contain functions directly related to a subcommand.
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


def info_command(modules: list[str], index: str = None) -> int:
    """
    Print module info.

    Parameters:
        modules (str): Module name or alias.
        index   (str): Specify index.

    Returns:
        int: Exit code.
    """
    return 0


def search_command(terms: list[str], index: str = None) -> int:
    """
    Search for modules.

    Should support shell-style wildcards (E.g. '*?')?

    Parameters:
        terms (list[str]): List of module names or aliases.
        index       (str): Specify index.

    Returns:
        int: Exit code.
    """
    return 0


def add_command(
    modules: list[str],
    index: str = None,
    git: bool = None,
    git_user_name: str = None,
    git_user_email: str = None,
    non_interactive: bool = False,
) -> int:
    """
    Add modules.

    Parameters:
        modules    (list[str]): List of names or aliases.
        index            (str): Specify index.
        git             (bool): Use git source control engine.
        git_user_name    (str): Specify git user name.
        git_user_email   (str): Specify git user email.
        non_interactive (bool): Use default parameters instead of prompts.

    Returns:
        int: Exit code.
    """
    return 0


def remove_command(
    modules: list[str],
    git: bool = None,
    git_user_name: str = None,
    git_user_email: str = None,
    non_interactive: bool = False,
):
    """
    Remove modules.

    Parameters:
        modules    (list[str]): List of names or aliases.
        git             (bool): Use git source control engine.
        git_user_name    (str): Specify git user name.
        git_user_email   (str): Specify git user email.
        non_interactive (bool): Use default parameters instead of prompts.

    Returns:
        int: Exit code.
    """
    return 0


def clean_command(
    git: bool = None,
    git_user_name: str = None,
    git_user_email: str = None,
    non_interactive: bool = False,
):
    """
    Clean modules.

    Remove modules that are no longer needed.

    Parameters:
        git             (bool): Use git source control engine.
        git_user_name    (str): Specify git user name.
        git_user_email   (str): Specify git user email.
        non_interactive (bool): Use default parameters instead of prompts.

    Returns:
        int: Exit code.
    """
    return 0


def update_command(
    modules: list[str],
    index: str = None,
    git: bool = None,
    git_user_name: str = None,
    git_user_email: str = None,
    non_interactive: bool = False,
):
    """
    Add modules.

    Parameters:
        modules    (list[str]): List of names or aliases.
        index            (str): Specify index.
        git             (bool): Use git source control engine.
        git_user_name    (str): Specify git user name.
        git_user_email   (str): Specify git user email.
        non_interactive (bool): Use default parameters instead of prompts.

    Returns:
        int: Exit code.
    """
    return 0
