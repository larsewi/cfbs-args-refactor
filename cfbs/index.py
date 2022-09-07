import logging as log

_DEFAULT_INDEX = (
    "https://raw.githubusercontent.com/cfengine/build-index/master/cfbs.json"
)


class Index:
    def __init__(self, index):
        if index:
            self._index = index
        else:
            self._index = _DEFAULT_INDEX
        log.debug("Loading index '%s'" % self._index)
