import os
import logging


LOGGER = logging.getLogger(__name__)


class FileService:
    """
    Service for writing message to a file.
    """
    @property
    def message(self) -> str:
        """
        Message, which is witten on the file.
        :return: ste
        """
        if self._message is None:
            self._message = "Hello"
        return self._message

    def __init__(self, message=None):
        self._message = message

    def run(self, path) -> None:
        """
        Run the service using a specified file,
        :param path: str
        :return: str
        """
        LOGGER.info("Writing '{}' to file {}.".format(self.message, path))

        with open(path, "w") as fp:
            fp.write(self.message)


class PingManager:
    """
    Manager that writes a message to a file, then pings an IRL and get the contents of the URL.
    """

    @property
    def file_service(self) -> FileService:
        """
        Get the FileService used by the manager.
        :return: FileService
        """
        if self._file_service is None:
            self._file_service = FileService()
        return self._file_service

    def __init__(self, file_service=None):
        self._file_service = file_service

    def run(self, path, url) -> None:
        """
        Run the manager with specific 'path' and 'url'.
        :param path: str
        :param url: str
        :return: None
        """

        LOGGER.info("Running manager ...")
        self.file_service.run(path)
