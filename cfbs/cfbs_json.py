from collections import OrderedDict


class CFBSJson:
    def __init__(self, data):
        self._data = data

    @staticmethod
    def create(index: str = None):
        pass

    @staticmethod
    def load(path):
        dct = load_json(path)
        mmodules= [Module(m) for m in dct["build"]]
        return CFBSJson(dct["name"],dct["desc"],modles)
        pass

    def save(self):
        pass

    @property
    def name(self):
        return self._data["name"]

    @property
    def description(self):
        return self._data["description"]

    @property
    def type(self):
        return self._data["type"]

    @property
    def git(self):
        return self._data["git"]

class Module:
    pass
