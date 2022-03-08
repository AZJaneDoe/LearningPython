#!/bin/python

################################################################################
# Programmer: Allie
# File: string_shifting.py
# Purpose: Take the string and shift the letters to the right by one
# Date: February 26, 2022
################################################################################

def main():
    # Given Username
    username = 'AbeSimp'

    # Want temp pass to be username with letters shifted to right
    password = ''
    # Loop through letters by index
    for i in range(len(username)):
        # Concatenate prev letter into string
        password += username[i-1]

    print(password)


if __name__ == '__main__':
    main()
