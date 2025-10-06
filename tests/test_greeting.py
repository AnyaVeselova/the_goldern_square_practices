from lib.greet import *

def test_greeting():
    result = greet("Anna")
    assert result == "Hello, Anna!"