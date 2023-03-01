# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 3/1/2023
# Description: Function that takes a string and returns a dictionary that tabulates how many
#              of each letter is in that string. The keys of diction should be upper-case.

def count_letters(string):
    """Returns a dictionary of how many of each letter is in a string."""
    string_dict = {}
    for ch in string.upper(): # make all upper-case letters
        if ch not in string_dict: # add letter to dictionary
            string_dict[ch] = 1
        else:
          string_dict[ch] += 1 # counting multiple letters

    return string_dict

# print(count_letters("AaBb"))
# testing