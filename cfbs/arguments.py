from argparse import ArgumentParser, BooleanOptionalAction
from typing import Dict

from cfbs.commands import *


def parse_args() -> Dict:
    parser = _create_parser()

    subparsers = parser.add_subparsers(title="commands")

    _add_init_command(subparsers)
    _add_status_command(subparsers)
    _add_info_command(subparsers)
    _add_search_command(subparsers)
    _add_add_command(subparsers)
    _add_remove_command(subparsers)
    _add_clean_command(subparsers)
    _add_update_command(subparsers)
    _add_pretty_command(subparsers)
    _add_validate_command(subparsers)
    _add_download_command(subparsers)

    args = parser.parse_args()
    return args


def _create_parser():
    parser = ArgumentParser(
        description="CFEngine build argument refactoring demo.",
    )
    parser.add_argument(
        "--log",
        default="info",
        choices=["critical", "error", "warning", "info", "debug"],
        help="select log level",
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="use default parameters instead of prompts",
    )
    return parser


# --- Arguments ---


def _add_git_arguments(parser):
    parser.add_argument(
        "--git", action=BooleanOptionalAction, help="use the git source control engine"
    )
    parser.add_argument("--git-user-name", help="specify git user name")
    parser.add_argument("--git-user-email", help="specify git user email")


# --- Subparsers ---


def _add_init_command(subparsers):
    parser = subparsers.add_parser("init", help="initialize project")
    parser.add_argument("--name", help="specify project name")
    parser.add_argument("--description", help="specify project description")
    parser.add_argument(
        "--masterfiles",
        action=BooleanOptionalAction,
        help="add default masterfiles policy framework",
    )
    parser.add_argument("--index", help="specify index")
    _add_git_arguments(parser)
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


def _add_status_command(subparsers):
    parser = subparsers.add_parser("status", help="print project status")
    parser.set_defaults(func=lambda _: status_command())


def _add_info_command(subparsers):
    parser = subparsers.add_parser("info", aliases=["show"], help="print module info")
    parser.add_argument("module", nargs="+", help="name or alias of module")
    parser.add_argument("--index", help="specify index")
    parser.set_defaults(func=lambda args: info_command(args.module, args.index))


def _add_search_command(subparsers):
    parser = subparsers.add_parser("search", help="search for modules")
    parser.add_argument("term", nargs="+", help="partial module name or alias")
    parser.add_argument("--index", help="specify index")
    parser.set_defaults(func=lambda args: search_command(args.term, args.index))


def _add_add_command(subparsers):
    parser = subparsers.add_parser("add", help="add modules")
    parser.add_argument("module", nargs="+", help="name or alias of module")
    parser.add_argument("--index", help="specify index")
    _add_git_arguments(parser)
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


def _add_remove_command(subparsers):
    parser = subparsers.add_parser("remove", help="remove modules")
    parser.add_argument("module", nargs="+", help="name or alias of module")
    parser.add_argument("--index", help="specify index")
    parser.set_defaults(
        func=lambda args: remove_command(
            args.module,
            args.git,
            args.git_user_name,
            args.git_user_email,
            args.non_interactive,
        )
    )


def _add_clean_command(subparsers):
    parser = subparsers.add_parser("clean", help="clean project")
    _add_git_arguments(parser)
    parser.set_defaults(
        func=lambda args: clean_command(
            args.git,
            args.git_user_name,
            args.git_user_email,
            args.non_interactive,
        )
    )


def _add_update_command(subparsers):
    parser = subparsers.add_parser("update", help="update modules")
    parser.add_argument("module", nargs="*", help="name or alias of module")
    parser.add_argument("--index", help="specify index")
    _add_git_arguments(parser)
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


def _add_pretty_command(subparsers):
    parser = subparsers.add_parser("pretty", help="format JSON files")
    parser.add_argument("file", nargs="+", help="path to file")
    parser.add_argument(
        "--check", action="store_true", help="check if files would be formatted"
    )
    parser.add_argument(
        "--keep-order", action="store_true", help="keep order of attributes"
    )
    _add_git_arguments(parser)
    parser.set_defaults(
        func=lambda args: pretty_command(
            args.file,
            args.check,
            args.keep_order,
            args.git,
            args.git_user_name,
            args.git_user_email,
            args.non_interactive,
        )
    )


def _add_validate_command(subparsers):
    parser = subparsers.add_parser("validate", help="validate cfbs resources")
    parser.add_argument("resource", help="resource path or URL")
    parser.add_argument(
        "--type", required=True, choices=["index", "policy-set", "module"]
    )
    parser.set_defaults(func=lambda args: validate_command(args.resouce, args.type))

def _add_download_command(subparsers):
    parser = subparsers.add_parser("download", help="download module dependencies")
    parser.add_argument("module", nargs="*", help="name or alias of module")
    parser.add_argument("--redownload", action="store_true", help="remove and download")
    parser.set_defaults(func=lambda args: download_command(args.module, args.redownload))
