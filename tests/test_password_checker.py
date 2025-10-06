from lib.password_checker import *
import pytest

def test_password_checker():
    checker = PasswordChecker()
    result = checker.check("54359076")
    assert result == True
    
def test_password_checker_more():
    checker = PasswordChecker()
    result = checker.check("543590760")
    assert result == True
    
def test_password_checker_less():
    checker = PasswordChecker()

    
    with pytest.raises(Exception) as e:
        checker.check("5432")
        
    msg = str(e.value)
    assert msg == "Invalid password, must be 8+ characters."
    
    