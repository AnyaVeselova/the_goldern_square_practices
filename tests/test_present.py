import pytest
from lib.present import Present


def test_present():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33
       
def test_without_wrap():
    present = Present() 
    with pytest.raises(Exception) as e:
         present.unwrap()
    
    message = str(e.value)
    assert message == "No contents have been wrapped."
    
def test_wrap_twice():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    
    message = str(e.value)
    assert message == "A contents has already been wrapped."
      
      
  
def test_wrap_twice_preserves_initial_val():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    
    
    assert present.unwrap() == 44
      
  
    