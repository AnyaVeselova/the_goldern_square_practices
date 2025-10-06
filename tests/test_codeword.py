from lib.check_codeword import *

def test_incorrect_codeword():
    result = check_codeword("Googlers 2025!")
    assert result == "WRONG!"

def test_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."
    

def test_correct_codeword():
    result = check_codeword("home")
    assert result == "Close, but nope."
    
def test_correct_first_letter():
    result = check_codeword("hot")
    assert result == "WRONG!"
    
    
def test_correct_last_letter():
    result = check_codeword("goose")
    assert result == "WRONG!"
    