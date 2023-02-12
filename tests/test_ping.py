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

