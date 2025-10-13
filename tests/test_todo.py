from lib.todo import *
import pytest
'''
Given no input returns raise an Exception
'''

def test_missing_task_arg_raises():
    with pytest.raises(TypeError):
        Todo() 
   

def test_check_initial_complete_value():
    todo = Todo("buy water")
    assert todo.task_dict["buy water"] == False
    
    
def test_mark_complete_as_true():
    todo = Todo("buy water")
    todo.mark_complete()
    assert todo.task_dict["buy water"] == True