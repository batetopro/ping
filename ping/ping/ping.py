import os


class FileService:
    @property
    def message(self):
        if self._message is None:
            self._message = "Hello"
        return self._message

    @property
    def path(self):
        if self._path is None:
            self._path = "hello.out"
        return self._path

    def __init__(self, path=None, message=None):
        self._path = path
        self._message = message

    def run(self):
        with open(self.path, "w") as fp:
            fp.write(self.message)


class PingManager:
    @property
    def file_service(self):
        if self._file_service is None:
            self._file_service = FileService()
        return self._file_service

    def __init__(self, file_service=None):
        self._file_service = file_service

    def run(self):
        self.file_service.run()
