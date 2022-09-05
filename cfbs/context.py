import logging as log

from cfbs.config import Config

class Context:
    def __init__(self, args):
        log.debug("Create context")
        self._args = args
        self._config = Config(args.index)
        self._files = []

    @property
    def args(self):
        return self.args

    @property
    def config(self):
        return self._config

    @property
    def commit(self):
        return self.files and self.args.git

    @property
    def files(self):
        return self._files