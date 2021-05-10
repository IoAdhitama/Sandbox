"""
The program will get input, and do the following using imported custom-made module:
- Return a list of all words ordered by the second letter from the left
- Will return the previous input (if any) if "previous" is the input
- Count the number of words and sentences
- Find all words with less than 5 letters
- Find all words with less than 5 letters, excluding vowels
"""

import string_data

user_input = ""

while user_input != "exit":

    user_input = string_data.get_input("Insert a sentence. Input 'exit' to exit: ")

    if user_input == "previous": # Return the previous input is "previous" is the input
        string_data.return_previous_input()
    elif user_input == "exit":
        break
    
    string_data.sort_by_second_letter()

    string_data.get_string_info()

    string_data.find_short_words()

    print(string_data.input_history)
