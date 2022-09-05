import logging as log
from cfbs.arguments import parse_args


def setup_logger(args):
    format = "%(levelname)8s: %(message)s"
    level = log._nameToLevel[args.log.upper()]
    log.basicConfig(format=format, level=level)


def main():
    args = parse_args()
    setup_logger(args)
    exit_status = args.func(args)
    return exit_status
