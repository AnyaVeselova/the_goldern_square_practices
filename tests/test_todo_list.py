from lib.todo_list import *
import pytest

'''
initial list should be an empty list
'''

def test_tasks_list():
    todo = TodoList()
    assert todo.tasks == []
    
    

