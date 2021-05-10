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


def find_short_words(): # Find all words that are shorter than 5 letters long
    words = input_history[-1].split(' ')

    print("List of words that are less than 5 letters:")
    for i in range(len(words)):
        if len(words[i]) < 5:
            print(words[i])

    print()

    # For each word in words, remove all the vowels
    words_without_vowels = []
    vowels = ('a', 'i', 'u', 'e', 'o')

    for word in words:
        for letter in word.lower():
            if letter in vowels:
                word = word.replace(letter, "")
        words_without_vowels.append(word)

    print(words_without_vowels)

    # Print words that are shorter than 5 letters long
    print("List of words that are less than 5 letters, excluding vowels:")
    for i in range(len(words)):
        if len(words_without_vowels[i]) < 5:
            print(words[i])
    print()