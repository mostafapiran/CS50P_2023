import pytest
from twttr import shorten


def test_assert():
    assert shorten("mostafa") == "mstf"
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("h3ll0 w0rld") == "h3ll0 w0rld"
    assert shorten("aeiou") == ""
    assert shorten("h@llo!!") == "h@ll!!"