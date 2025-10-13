# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, todo):
        self.tasks.append(todo)

    def incomplete(self):
        return list(filter(
        lambda task_dict: any(value is False for value in task_dict.values()),
        self.tasks
    ))
        
    def complete(self):
        return list(filter(
        lambda task_dict: any(value is True for value in task_dict.values()),
        self.tasks))

    def give_up(self):
       for task in self.tasks:
        for key in task:
            task[key] = True

