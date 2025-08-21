from twttr import shorten
import pytest

def test_combination():
    assert shorten("SaBiK") == "SBK"

def test_lower():
    assert shorten("sabik") == "sbk"

def test_upper():
    assert shorten("SABIK") == "SBK"

def test_nletter():
    assert shorten("sab12") == "sb12"

def test_punctu():
    assert shorten("sabik!") == "sbk!"
with pytest.raises(TypeError):
     shorten(1)
