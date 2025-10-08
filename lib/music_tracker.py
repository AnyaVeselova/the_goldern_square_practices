import pytest

class MusicTracker:

    def __init__(self):
        self.song_list = []

    def add(self, song):
        if type(song) != str:
            raise Exception("Input must be a string")
        elif song == "":
            raise Exception("Input must not be empty")
        else:
            self.song_list.append(song)
            

    def list_songs(self):
        if len(self.song_list) == 0:
            raise Exception("Add a song first!")
        return self.song_list
