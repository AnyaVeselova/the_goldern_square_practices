
## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

_As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
_

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:


    def __init__(self):
        # Side effects:
        #  initialises the music list
        pass

    def add(self, song):
        # Parameters:
        #   song: a string representing a song
        #   Saves the song to the music list
        pass # No code here yet

    def list_songs(self):
        # Returns: a list of songs
    
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given an input that is not a string, it rases an EXception
"""
music_tracker = MusicTracker()
music_tracker.add(0) # => raises Exception


"""
Given a song as a parameter it add this song to the list
"""
music_tracker = MusicTracker()
music_tracker.add("Paradise") # => ["Paradise]


"""
Given an empty string into the add method, it rases an Exception
"""
music_tracker = MusicTracker()
music_tracker.add("") # => raises Exception

"""
Given a song as a parameter it add this song to the list
"""
music_tracker = MusicTracker()
music_tracker.add("Paradise") # => ["Paradise]
music_tracker.add("Colours")
music_tracker.list_songs() # => ["Paradise", "Colours"] 

"""
Raises an Exception when the list is empty and the list_music is called first
"""
"""
Given an empty string into the add method, it rases an Exception
"""
music_tracker = MusicTracker()
music_tracker.list_music() # => raises Exception

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

