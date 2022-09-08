CFBS_JSON_PROJECT_TYPES = ["index", "policy-set", "module"]


class CFBSModule:
    def __init__(self, data):
        self._data = data

    @property
    def name(self) -> str:
        """
        Return:
            str: Module name.
        """
        return self._data["name"]

    @property
    def description(self) -> str:
        """
        Return:
            str: Module description.
        """
        return self._data["description"]

    @property
    def tags(self) -> list[str]:
        """
        Return:
            list[str]: Module tags.
        """
        return self._data["tags"]

    @property
    def repo(self) -> str:
        """
        Return:
            str: Repository containing module.
        """
        return self._data["repo"]

    @property
    def url(self) -> str:
        """
        Return:
            str: URL to module.
        """
        return self._data["url"]

    @property
    def path(self) -> str:
        """
        Return:
            str
        """

    @property
    def by(self) -> str:
        """
        Return:
            str: Name of module creator.
        """
        return self._data["by"]

    @property
    def version(self) -> str:
        """
        Return:
            str: Module version.
        """
        return self._data["version"]

    @property
    def commit(self) -> str:
        """
        Return:
            str: Commit SHA related to module version.
        """
        return self._data["commit"]

    @property
    def subdirectory(self) -> str:
        """
        Return:
            str: Subdirectory path of module.
        """
        return self._data["subdirectory"]

    @property
    def steps(self) -> list[str]:
        """
        Return:
            list[str]: Module build steps.
        """
        return self._data["steps"]

    @property
    def dependencies(self) -> list[str]:
        """
        Return:
            list[str]: Module dependencies.
        """
        return self._data["dependencies"]

    @property
    def added_by(self) -> str:
        """
        Return:
            str: What module or command added this module.
        """
        return self._data["added_by"]



class CFBSBuild:
    def __init__(self, data):
        self._data = data

    def __getitem__(self, index):
        return CFBSModule(self._data[index])

    def __iter__(self):
        self._iter_index = 0
        self._iter_stop = len(self._data)
        return self

    def __next__(self) -> CFBSModule:
        if self._iter_index >= self._iter_stop:
            raise StopIteration
        module = CFBSModule(self._data[self._iter_index])
        self._iter_index += 1
        return module

    def append(self, module: CFBSModule):
        self._data.append(module._data)


class CFBSJson:
    def __init__(self, data):
        self._data = data

    @staticmethod
    def create(index: str = None):
        pass

    @staticmethod
    def load(path):
        pass

    def save(self):
        pass

    @property
    def name(self):
        """
        Returns:
            str: Project name.
        """
        return self._data["name"]

    @property
    def description(self):
        """
        Returns:
            str: Project description.
        """
        return self._data["description"]

    @property
    def type(self):
        """
        Returns:
            str: Project type.
        """
        return self._data["type"]

    @property
    def git(self):
        """
        Returns:
            bool: True if git is enabled for project.
        """
        return self._data["git"]

    @property
    def index(self):
        """
        URL, relative path, or inline dictionary. Used by cfbs add and cfbs
        search, when index key is present in cfbs.json in the current working
        directory. When adding a module by URL, which has a cfbs.json inside of
        it, the index in that file should be ignored.
        """
        pass

    @property
    def provides(self):
        pass

    @property
    def build(self):
        """
        Returns:
            CFBSBuild: List of modules in build.
        """
        return CFBSBuild(self._data["build"]) if "build" in self._data else None
