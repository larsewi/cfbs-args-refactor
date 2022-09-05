import logging as log

from cfbs.index import Index


class Config:
    def __init__(self, index):
        self._path = "cfbs.json"
        log.debug("Loading config '%s'" % self._path)

        self._index = Index(index)

    def save(self):
        log.debug("Saving config '%s'" % self._path)
