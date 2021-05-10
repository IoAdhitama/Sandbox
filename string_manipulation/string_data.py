input_history = []

def get_input(string_input):
    input_history.append(string_input)

def input_process(sentence): # Process the input and return list of words ordered by second letter
    sentence.split()
    print(sentence)

def return_previous_input(): # Return the previous input.
    if len(input_history) <= 1:
        print("No input in history.")
    else:
        print(input_history[len(input_history)])