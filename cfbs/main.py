import logging as log
from cfbs.arguments import parse_args


def setup_logger(log_debug: bool = False):
    format = "%(levelname)8s: %(message)s"
    level = log.DEBUG if log_debug else log.INFO
    log.basicConfig(format=format, level=level)


def main():
    args = parse_args()
    setup_logger(args.log_debug)
    args.func(args)
    return 0
