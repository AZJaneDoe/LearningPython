#!/bin/python

################################################################################
# Programmer: Allie
# File: range_len_function.py
# Purpose: How do Range and len functions work
# Date: February 26, 2022
################################################################################


def main():
    # Your code here

    # Prints 01234; 0 -> end -1
    for i in range(5):
        print(i)

    str = 'string'
    # Prints the length of the *iteratble* variable
    print(len(str))

    # "len(str)" -> number of items in string
    # "range(end)" -> 0 -> end - 1
    # range(len(var) -> 0 to number of items in var - 1
    for i in range(len(str)):
        print(i)

    # Print each letter corresponding to the index of the string
    for i in range(len(str)):
        print(str[i])


if __name__ == '__main__':
    main()
