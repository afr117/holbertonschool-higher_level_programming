#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list of booleans to store whether each element is divisible by 2
    result = []
    # Iterate through the elements in the input list
    for number in my_list:
        # Check if the number is divisible by 2
        if number % 2 == 0:
            result.append(True)
        else:
            result.append(False)    
    return result

