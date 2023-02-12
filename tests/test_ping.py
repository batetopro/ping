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
