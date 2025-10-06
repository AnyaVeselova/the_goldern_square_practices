from lib.string_builder import *


def test_initial_output():
    string = StringBuilder()
    result = string.output()
    assert result == ""


def test_string_builder():
    string = StringBuilder()
    string.add("Hello")
    string.add(" World!")
    result = string.output()
    assert result == "Hello World!"
    
    
def test_string_builder_len():
    string = StringBuilder()
    string.add("Hello")
    string.add(" World!")
    result = string.size()
    assert result == 12