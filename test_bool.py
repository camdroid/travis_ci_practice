import main
import unittest

def test_main():
    assert main.main() is True


def test_no():
    assert main.no() is False

