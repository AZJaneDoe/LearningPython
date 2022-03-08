#!/bin/python

################################################################################
# Programmer: Allie
# File: common_letters.py
# Purpose: Find common letters or words between two words
# Date: February 26, 2022
################################################################################

def contains(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False


print(contains("watermelon", "melon"))
print(contains("watermelon", "berry"))


def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if letter in string_two:
            if letter not in common:
                common.append(letter)
    if len(common):
        return common
    else:
        return 'No common letters'


print(common_letters("banana", "cream"))
