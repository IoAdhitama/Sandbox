"""
The program will get input, and do the following using imported custom-made module:
- Return a list of all words ordered by the second letter from the left
- Will return the previous input (if any) if "previous" is the input
- Count the number of words and sentences
- Find all words with less than 5 letters
- Find all words with less than 5 letters, excluding vowels
"""

import string_data


string_data.get_input("Insert a sentence: ")
print(string_data.input_history)
