from lib.count_words import *
import pytest

def test_input():
    
    with pytest.raises(TypeError) as exc_info:
        count_words(234234)
        
    assert "must be a string" in str(exc_info.value)
    
def test_empty_string():
    result = count_words("")
    assert result == 0


def test_count_words():
    result = count_words("Count these words")
    assert result == 3
    
    
def test_multiple_spaces():
    result = count_words("   too   many   spaces   ")
    assert result == 3

def test_punctuation():
    result = count_words("Hello, world!")
    assert result == 2
    
def test_newlines_and_tabs():
    result = count_words("Hello\nworld\tPython")
    assert result == 3

def test_single_word():
    result = count_words("Hello")
    assert result == 1

def test_apostrophes_and_hyphens():
    result = count_words("It's a well-known fact.")
 
    assert result == 6  # for pure \w+ behavior
