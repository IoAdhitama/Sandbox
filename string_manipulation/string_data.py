input_history = []

def get_input(input_prompt):
    string_input = input(input_prompt)
    input_history.append(string_input)
    return string_input

def sort_by_second_letter(sentence): # Process the input and return list of words ordered by second letter
    sentence.split()
    print(sentence)

def return_previous_input(): # Return the previous input.
    if len(input_history) <= 1:
        print("No input in history.")
    else:
        print(input_history[len(input_history)])