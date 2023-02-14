#!/usr/bin/env python

"""Tests for `ping` package."""

import os


from ping import ping


def test_file_service():
    service = ping.FileService()
    path = "hello.out"

    service.run(path)

    try:
        with open(path, "r") as fp:
            data = fp.read()
        assert data == service.message
    finally:
        os.unlink(path)

def test_ping_service():
    service = ping.PingService()
    assert True == service.run("google.com")
    assert True == service.run("194.153.145.104")
    assert True == service.run("https://stackoverflow.com/questions/2953462/pinging-servers-in-python")
    assert True == service.run("https://151.101.65.69/questions/2953462/pinging-servers-in-python")
    assert False == service.run("http://overthehillsandfarawy.com/")
    assert False == service.run("129.0.0.1")


def test_http_get_service():
    service = ping.HttpGetService()
    response = service.run("https://docs.python.org/3/howto/argparse.html")
    assert 200 == response.status_code
    assert 0 < response.content_length

    response = service.run("https://docs.python.org/3/howto/argparse.sdfsdf")
    assert 404 == response.status_code

def test_ping_manager():
    manager = ping.PingManager()
    response = manager.run("hello.out", "https://docs.python.org/3/howto/argparse.html")
    assert 200 == response.status_code
    assert 0 < response.content_length

    response = manager.run("hello.out", "http://overthehillsandfarawy.com/")
    assert response is None
