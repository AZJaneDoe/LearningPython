# #!/bin/python

# ################################################################################
# # Programmer: Allie
# # File: Day_1_Band_Name_Generator.py
# Coding Exercise 1.1: Counting Number of Letters in Name
# Coding Project 1.A: Band Name Generator
# # Subjects: Print, Input, Variables, New Lines (\n)
# # Date: February 27, 2022
# ################################################################################

# # This Print statement will ask the question 'What is your name?'
# # The response in the terminal will be used to say Hello afterwards
print("Hello " + input("What is your name ?"))
# # Or using a variable to save data
name1 = input("What is your name ?")
print(name1)


# # Coding Exercise 1.1: Counting Number of Letters in Name
# # Using the len and input function
#   # "What is your name ?" is the question printed
#   # Input takes the answer in the terminal
#   # Len takes the input answer in the terminal and prints out the number of items of an object
print(len(input("What is your name ?")))
# # Or using a variable to save data
name2 = input("What is your name ?")
print(name2)

# #Variables
a = input("a:")
b = input("b:")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)

# Coding Project 1.A: Band Name Generator
# 1. Create a greeting
print("Welcome to the Band Name Generator.")
# 2. Ask the User for the City that they grew up in.
city = input("What's the name of the city you grew up in ? \n")
# 3. Ask the user for the name of a pet
pet = input("Please name an animal. \n")
# # 4. Combine the name of their city and pet and show them their band name
print("A band name option is " + str(city) + " " + str(pet))


# 5. Make sure the input cursor shows on a new line
