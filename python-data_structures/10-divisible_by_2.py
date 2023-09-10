#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list to store True or False values
    result = []
    # Iterate through the original list and check if each element is divisible by 2
    for num in my_list:
        result.append(num % 2 == 0)
    return result
