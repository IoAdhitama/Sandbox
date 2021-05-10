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

def sort_by_second_letter(): # Process the input and return list of words ordered by second letter
    words = input_history[-1].split()
    words.sort(key = get_second_letter)

    print("List of all words ordered by the second letter from the left: ")
    for i in range(len(words)):
        print(words[i])

    print()

def return_previous_input(): # Return the previous input.
    if len(input_history) == 0:
        print("No input in history.")
    else:
        input_history.pop()
        print(input_history[-1])

def get_string_info(): # Count the number of words and sentences in the input
    sentences = input_history[-1].split('. ')
    words = input_history[-1].split(' ')

    # Remove any empty list entry
    [sentences.pop(i) for i in range(len(sentences)) if sentences[i] == '']
    [words.pop(i) for i in range(len(words)) if words[i] == '']

    print("The number of sentence in the input is {}.".format(len(sentences)))
    print("The number of words in the input is {}.".format(len(words)))
    print()