from lib.letter_counter import *


def test_letter_counter():   
    counter = LetterCounter("Digital Punk")
    assert counter.calculate_most_common() == [2, "i"]

def test_letter_counter_2():   
    counter = LetterCounter("Join a meeting")
    assert counter.calculate_most_common() == [2, "e"]

def test_letter_counter_3():   
    counter = LetterCounter("")
    assert counter.calculate_most_common() == [0, None]