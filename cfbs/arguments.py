from argparse import ArgumentParser, BooleanOptionalAction
from typing import Dict

from cfbs.commands import *


def parse_args() -> Dict:
    main_parser = _main_parser()

    subparsers = main_parser.add_subparsers(title="subcommands")
    _init_subparser(subparsers)
    _status_subparser(subparsers)
    _info_subparser(subparsers)
    _search_subparser(subparsers)
    _add_subparser(subparsers)
    _remove_subparser(subparsers)
    _clean_subparser(subparsers)
    _update_command(subparsers)

    args = main_parser.parse_args()
    return args


def _main_parser():
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


def _init_subparser(subparsers):
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


def _status_subparser(subparsers):
    parser = subparsers.add_parser("status", help="print project status")
    parser.set_defaults(func=lambda _: status_command())


def _info_subparser(subparsers):
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


def _search_subparser(subparsers):
    parser = subparsers.add_parser("search", help="search for modules in index")
    parser.add_argument("terms", nargs="*", help="name of module to add")
    _index_arguments(parser)
    parser.set_defaults(func=search_command)


def _add_subparser(subparsers):
    parser = subparsers.add_parser("add", help="add a module")
    parser.add_argument("name", nargs="*", help="name of module to add")
    _index_arguments(parser)
    _git_arguments(parser)
    parser.set_defaults(func=add_command)


def _remove_subparser(subparsers):
    parser = subparsers.add_parser("remove", help="remove a module")
    parser.add_argument("name", nargs="*", help="name/alias of module to remove")
    _index_arguments(parser)
    _git_arguments(parser)
    parser.set_defaults(func=remove_command)


def _clean_subparser(subparsers):
    parser = subparsers.add_parser(
        "clean", help="remove modules that are no longer needed"
    )
    _index_arguments(parser)
    _git_arguments(parser)
    parser.set_defaults(func=clean_command)


def _update_command(subparsers):
    parser = subparsers.add_parser("update", help="update modules")
    parser.add_argument("name", nargs="*", help="name/alias of module to update")
    _index_arguments(parser)
    _git_arguments(parser)
    parser.set_defaults(func=update_command)
