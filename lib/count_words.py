import re

def count_words(input_val):
    if not isinstance(input_val, str):
        raise TypeError("Input must be a string")
    
    return len(re.findall(r'\b\w+\b', input_val))