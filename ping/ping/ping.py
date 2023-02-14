import platform
import subprocess
import logging
from urllib.parse import urlparse
import dataclasses


import requests


LOGGER = logging.getLogger(__name__)


class FileService:
    """
    Service for writing message to a file.
    """
    @property
    def message(self) -> str:
        """
        Message, which is witten on the file.
        :return: str
        """
        if self._message is None:
            self._message = "Hello"
        return self._message

    def __init__(self, message=None):
        self._message = message

    def _do_write(self, path) -> None:
        with open(path, "w") as fp:
            fp.write(self.message)

    def run(self, path) -> None:
        """
        Run the service using a specified file,
        :param path: str
        :return: None
        """
        LOGGER.info("Writing '{}' to file {}.".format(self.message, path))
        self._do_write(path)


class PingService:
    """
    Service for pinging host of a given URL.
    """
    @classmethod
    def get_domain(cls, url) -> str:
        """
        Get the domain of a given URL.
        :param url: str
        :return: str
        """
        parsed_url = urlparse(url)
        if not parsed_url.netloc:
            return parsed_url.path
        return parsed_url.netloc

    @classmethod
    def _do_ping(cls, host) -> bool:
        """
        Make a ping to a given host.
        Returns True if host (str) responds to a ping request.
        Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
        :param host: str
        :return: bool
        """
        LOGGER.info("Calling ping for host '{}' ...".format(host))

        # Option for the number of packets as a function of
        flag = "-c"
        if platform.system().lower()=='windows':
            flag = '-n'

        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', flag, '1', host]

        result = subprocess.call(command)

        LOGGER.info("Ping result for host '{}': {}.".format(host, result))

        return result == 0


    def run(self, url) -> bool:
        """
        Pings the domain of a given URL.
        :param url: str
        :return: bool
        """
        LOGGER.info("Pinging '{}' ...".format(url))
        domain = self.get_domain(url)
        return self._do_ping(domain)


@dataclasses.dataclass
class GetResponse:
    """
    Container for data received from HttpGetService.
    """

    status_code: int
    content_length: int
    url: str

    def log(self) -> None:
        """
        Log the response.
        :return: None
        """
        LOGGER.info("GET response from '{}' with status code {} and content-length {}.".format(
            self.url, self.status_code, self.content_length
        ))


class HttpGetService:
    """
    Service for making HTTP GET requests to a given URL.
    """
    def run(self, url):
        LOGGER.info("Sending GET request to {} ...".format(url))
        response = requests.get(url, stream=True)
        result = GetResponse(
            status_code=response.status_code,
            content_length=int(response.headers.get("Content-Length", 0)),
            url=response.url,
        )
        result.log()
        return result


class PingManager:
    """
    Manager that writes a message to a file, then pings an URL and get the contents of the URL.
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

    @property
    def ping_service(self) -> PingService:
        """
        Get the PingService used by the manager.
        :return: PingService
        """
        if self._ping_service is None:
            self._ping_service = PingService()
        return self._ping_service

    @property
    def http_get_service(self) -> HttpGetService:
        """
        Get the HttpGetService used by the manager.
        :return: HttpGetService
        """
        if self._http_get_service is None:
            self._http_get_service = HttpGetService()
        return self._http_get_service

    def __init__(self, file_service=None, ping_service=None, http_get_service=None):
        """
        Initialize the manager
        :param file_service: FileService
        :param ping_service: PingService
        :param http_get_service: HttpGetService
        """
        self._file_service = file_service
        self._ping_service = ping_service
        self._http_get_service = http_get_service

    def run(self, path, url) -> GetResponse:
        """
        Run the manager with specific 'path' and 'url'.
        :param path: str
        :param url: str
        :return: GetResponse | None
        """
        result = None
        LOGGER.info("Running manager ...")
        self.file_service.run(path)
        if self.ping_service.run(url):
            result = self.http_get_service.run(url)
        return result
