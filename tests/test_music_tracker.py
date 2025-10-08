import pytest
from lib.music_tracker import *

def test_music_tracker_input():
    
    music_tracker = MusicTracker()
    
    with pytest.raises(Exception) as e:
        music_tracker.add(0)
        
    assert "Input must be a string" == str(e.value)
    
    music_tracker.add("Paradise")
    
    assert "Paradise" in music_tracker.list_songs()
    
    with pytest.raises(Exception) as e:
        music_tracker.add("")
    assert "Input must not be empty" == str(e.value)
    

def test_music_tracker_list():
    music_tracker = MusicTracker()
    music_tracker.add("Paradise") 
    music_tracker.add("Colours")
    list_songs = music_tracker.list_songs() 

    assert list_songs == ["Paradise", "Colours"]
    
    music_tracker_2 = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker_2.list_songs()
        
    assert "Add a song first!" == str(e.value)