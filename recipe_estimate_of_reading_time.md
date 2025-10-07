
## 1. Describe the Problem

_As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute_

## 2. Design the Function Signature

```python
# EXAMPLE

def estimate_reading_time(text):
    """
    # Parameters:
    # text: a string

    #  Returns: a float representing a reading time

    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text of 200 words it will return a reading time of 1
"""
estimate_reading_time("...200..."): => 1.0


"""
Given a text of 400 words it will return a reading time of 1.5
"""
estimate_reading_time("...300..."): => 1.5

"""
Given an empty string it will raise and arror
"""
estimate_reading_time(""): => "Error: Can't estimate reading time for an empty text."