"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def is_contiguous_sublist(small_list, big_list):
    """
    Helper function to determine if small_list is a contiguous sublist of big_list.
    """
    if not small_list:
        return True
    if len(small_list) > len(big_list):
        return False
        
    # Iterate through all possible starting points in the big_list
    for i in range(len(big_list) - len(small_list) + 1):
        # Check if the slice of big_list matches small_list
        if big_list[i:i + len(small_list)] == small_list:
            return True
    return False


def sublist(list_one, list_two):
    """
    Determines the relationship between two lists: equal, sublist, superlist, or unequal.
    """
    if list_one == list_two:
        return EQUAL

    if is_contiguous_sublist(list_one, list_two):
        return SUBLIST

    if is_contiguous_sublist(list_two, list_one):
        return SUPERLIST

    return UNEQUAL