# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        
        self.task = task
        self.complete = False
        
        self.task_dict = {
            self.task: self.complete
        }




    def mark_complete(self):
        self.task_dict[self.task] = True

