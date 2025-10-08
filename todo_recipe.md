
## 1. Describe the Problem

_As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list._

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class ToDo:

    def __init__(self, list):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def add(self, task):
        # Parameters: 
        # task: str, representing a task
        pass
    def list_incomplete(self):
        # Returns:
        # A list of incomlete tasks

    def mark_complete(self, index):
        # Parameters:
        # index: and integer representing the task to comlete
        # side-effect:
        # removes the task at index from the list of the tasks
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Initially, there are no tasks
"""
tracker = TaskTracker()
tracker.list_incomplete() # => []

"""
When we add a task 
It is reflected in the list of tasks
"""

tracker = TaskTracker()
tracker.add("Walk the dog") 
tracker.list_incomplete() # => ["Walk the dog"]

"""
When we add multiple tasks
They all are reflected in the list of tasks
"""
tracker = TaskTracker()
tracker.add("Walk the dog") 
tracker.add("Walk the cat") 
tracker.add("Walk the frog") 
tracker.list_incomplete() # => ["Walk the dog", "Walk the cat", "Walk the frog"]




_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

