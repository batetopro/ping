# ping
## Task
Create a Python script that can run on Windows, Linux, and Mac that will:
1. Create a text file containing Hello (file path should be command line argument)
2. Ping and request.get an IP (should be command line argument) 
3. Run test.bat on Windows or test.sh on Linux/Mac

## Commands
To run the test command:
```commandline
./test.sh
```

To run the pacakge CLI command:
```commandline
python ping/ping/cli.py [-h] [-f FILE] url
```
To build the documentation:
```commandline
make docs
```
To run tests:
```commandline
make test
```
To run test coverage:
```commandline
make coverage
```

## Package

![class_diagram](https://github.com/batetopro/ping/raw/main/assets/class_diagram.png)

The package contains:
* FileService - Service for writing message to a file.
* PingService - Service for pinging host of a given URL.
* HttpGetService - Service for making HTTP GET requests to a given URL.
* GetResponse - Container for data received from HttpGetService.
* PingManager - Manager that writes a message to a file, then pings an URL 
and get the contents of the URL.