#!/usr/bin/python3

def multiple_returns(sentence):
    # Calculate the length of the sentence
    length = len(sentence)

    # Set the first character to None if the sentence is empty
    first = sentence[0] if length > 0 else None

    return length, first

# Example usage
if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))

