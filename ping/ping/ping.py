import os
import logging


LOGGER = logging.getLogger(__name__)


class FileService:
    @property
    def message(self):
        if self._message is None:
            self._message = "Hello"
        return self._message

    def __init__(self, message=None):
        self._message = message

    def run(self, path):
        LOGGER.info("Writing '{}' to file {}.".format(self.message, path))

        with open(path, "w") as fp:
            fp.write(self.message)


class PingManager:
    @property
    def file_service(self):
        if self._file_service is None:
            self._file_service = FileService()
        return self._file_service

    def __init__(self, file_service=None):
        self._file_service = file_service

    def run(self, path, url):
        LOGGER.info("Running manager ...")
        self.file_service.run(path)
