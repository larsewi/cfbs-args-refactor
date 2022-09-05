import time
import logging as log

from cfbs.context import Context


def command_wapper(func):
    def inner(args):
        begin = time.time()
        log.debug("Begin '%s'" % func.__name__)

        ctx = Context(args)
        exit_status = func(ctx)
        assert isinstance(exit_status, int)
        if exit_status == 0:
            ctx.config.save()
            if ctx.commit:
                log.debug("Performing 'git add %s'" % ctx.files.join(" "))
                log.debug("Performing 'git commit'")
            exit_status = 0

        log.debug("End '%s'" % func.__name__)
        log.debug("Execution time: %f s" % (time.time() - begin))
        log.debug("Exit status: %d" % exit_status)

        return exit_status
    return inner


@command_wapper
def init_command(ctx):
    return 0


@command_wapper
def status_command(ctx):
    return 0


@command_wapper
def search_command(ctx):
    return 0


@command_wapper
def add_command(ctx):
    return 0


@command_wapper
def remove_command(ctx):
    return 0


@command_wapper
def clean_command(ctx):
    return 0

@command_wapper
def update_command(ctx):
    return 0
