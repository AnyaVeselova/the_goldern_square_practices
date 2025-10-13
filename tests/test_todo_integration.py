from lib.todo_list import *
from lib.todo import *
import pytest


''''
Given an instance of Todo() adds it to the tasks_list and returns nothing
'''

def test_check_add_task():
    todo = Todo("Jump")
    todo_list = TodoList()
    todo_list.add(todo.task_dict)
    print(todo_list.tasks)
    assert todo_list.tasks == [{"Jump": False}]
    
''''
List all the tasks which are incomplete (task.complete = True)
'''

def test_check_incomplete():
    todo_1 = Todo("Jump")
    todo_2 = Todo("Swim")
    todo_list = TodoList()
    todo_list.add(todo_1.task_dict) 
    todo_list.add(todo_2.task_dict)
    todo_1.mark_complete()
    assert todo_list.incomplete() == [{"Swim": False}]
   
   

def test_check_complete():
    todo_1 = Todo("Jump")
    todo_2 = Todo("Swim")
    todo_list = TodoList()
    todo_list.add(todo_1.task_dict) 
    todo_list.add(todo_2.task_dict)
    todo_1.mark_complete()
    assert todo_list.complete() == [{"Jump": True}]
   
   
def test_check_give_up():
    todo_1 = Todo("Jump")
    todo_2 = Todo("Swim")
    todo_list = TodoList()
    todo_list.add(todo_1.task_dict) 
    todo_list.add(todo_2.task_dict)
    todo_list.give_up()
    assert todo_list.tasks == [{"Jump": True}, {"Swim": True}]
