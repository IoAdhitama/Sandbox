input_history = []

def get_input(input_prompt):
    string_input = input(input_prompt)
    input_history.append(string_input)
    return string_input

def get_second_letter(word):
    if len(word) < 2: # Check whether the word has at least 2 letters
        return word
    else:
        return word[1]

def sort_by_second_letter(sentence): # Process the input and return list of words ordered by second letter
    words = sentence.split()
    words.sort(key = get_second_letter)

    print("List of all words ordered by the second letter from the left: ")
    for i in range(len(words)):
        print(words[i])

def return_previous_input(): # Return the previous input.
    if len(input_history) <= 1:
        print("No input in history.")
    else:
        print(input_history[len(input_history)])