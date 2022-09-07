from argparse import ArgumentParser, BooleanOptionalAction
from typing import Dict

from cfbs.commands import *


def parse_args() -> Dict:
    parser = _create_parser()

    subparsers = parser.add_subparsers(title="subcommands")

    _init_subcommand(subparsers)
    _status_subcommand(subparsers)
    _info_subcommand(subparsers)
    _search_subcommand(subparsers)
    _add_subcommand(subparsers)
    _remove_subcommand(subparsers)
    _clean_subcommand(subparsers)
    _update_subcommand(subparsers)

    args = parser.parse_args()
    return args


def _create_parser():
    parser = ArgumentParser(
        description="CFEngine build argument refactoring demo.",
        epilog="Use 'cfbs help -a' to list available low-level commands.",
    )
    parser.add_argument(
        "--log",
        default="info",
        choices=["critical", "error", "warning", "info", "debug"],
        help="select log level",
    )
    parser.add_argument(
        "--non-interactive",
        default=False,
        help="use default parameters instead of prompts",
    )
    return parser


# --- Arguments ---


def _git_arguments(parser):
    parser.add_argument(
        "--git", action=BooleanOptionalAction, help="use the git source control engine"
    )
    parser.add_argument("--git-user-name", help="specify git user name")
    parser.add_argument("--git-user-email", help="specify git user email")


def _index_arguments(parser):
    parser.add_argument("--index", help="specify index")


# --- Subparsers ---


def _init_subcommand(subparsers):
    parser = subparsers.add_parser("init", help="initialize a cfbs project")
    parser.add_argument("--name", help="specify project name")
    parser.add_argument("--description", help="specify project description")
    parser.add_argument(
        "--masterfiles",
        action=BooleanOptionalAction,
        help="add default masterfiles policy framework",
    )
    _index_arguments(parser)
    _git_arguments(parser)
    parser.set_defaults(
        func=lambda args: init_command(
            args.name,
            args.description,
            args.index,
            args.masterfiles,
            args.git,
            args.git_user_name,
            args.git_user_email,
            args.non_interactive,
        )
    )


def _status_subcommand(subparsers):
    parser = subparsers.add_parser("status", help="print project status")
    parser.set_defaults(func=lambda _: status_command())


def _info_subcommand(subparsers):
    parser = subparsers.add_parser(
        "info", aliases=["show"], help="print project status"
    )
    parser.add_arugment(
        "module",
        nargs="+",
        help="module name or alias",
    )
    _index_arguments(parser)
    parser.set_defaults(func=lambda args: info_command(args.module, args.index))


def _search_subcommand(subparsers):
    parser = subparsers.add_parser("search", help="search for modules")
    parser.add_argument("term", nargs="+", help="partial module name or alias")
    _index_arguments(parser)
    parser.set_defaults(func=lambda args: search_command(args.term, args.index))


def _add_subcommand(subparsers):
    parser = subparsers.add_parser("add", help="add modules")
    parser.add_argument("module", nargs="+", help="name or alias of module to add")
    _index_arguments(parser)
    _git_arguments(parser)
    parser.set_defaults(
        func=lambda args: add_command(
            args.module,
            args.index,
            args.git,
            args.git_user_name,
            args.git_user_email,
            args.non_interactive,
        )
    )


def _remove_subcommand(subparsers):
    parser = subparsers.add_parser("remove", help="remove modules")
    parser.add_argument("module", nargs="+", help="name or alias of module to remove")
    _git_arguments(parser)
    parser.set_defaults(
        func=lambda args: remove_command(
            args.module,
            args.git,
            args.git_user_name,
            args.git_user_email,
            args.non_interactive,
        )
    )


def _clean_subcommand(subparsers):
    parser = subparsers.add_parser(
        "clean", help="remove modules that are no longer needed"
    )
    _git_arguments(parser)
    parser.set_defaults(
        func=lambda args: clean_command(
            args.git,
            args.git_user_name,
            args.git_user_email,
            args.non_interactive,
        )
    )


def _update_subcommand(subparsers):
    parser = subparsers.add_parser("update", help="update modules")
    parser.add_argument("", nargs="+", help="name/alias of module to update")
    _index_arguments(parser)
    _git_arguments(parser)
    parser.set_defaults(
        func=lambda args: update_command(
            args.module,
            args.index,
            args.git,
            args.git_user_name,
            args.git_user_email,
            args.non_interactive,
        )
    )
