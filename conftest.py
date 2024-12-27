from base64 import b64encode

import pytest


@pytest.fixture
def shared_secret():
    return b64encode(b"1234567890abcdefghij")


@pytest.fixture
def identity_secret():
    return b64encode(b"abcdefghijklmnoprstu")
