# #!/bin/python

# ################################################################################
# # Programmer: Allie
# # File: Day_3_Treasure_Island.py
# Coding Exercise 3.1: Odd or Even
# Coding Exercise 3.2: BMI 2.0
# Coding Exercise 3.3: Leap Year
# Coding Exercise 3.4: Pizza Order Practice
# Coding Exercise 3.5: Love Calculator
# Coding Project 3.A: Treasure Island
# # Subjects: Conditional Statements, Logical Operators, Code Blocks, and Scope
# # Date: March 1, 2022
# ################################################################################

# Conditional Statements: If/Else Format
#   if condition:
#      do this
#   else:
#      do this
# Coding Exercise 3.1: Odd or Even
number = int(input("Which number do you want to check? "))
num_div = number % 2

if num_div == 1:
    print("This is an odd number")
else:
    print("This is an even number")


# Coding Exercise 3.2: BMI 2.0
height = input("enter your height in m:")
weight = input("enter your height in kg:")
bmi_calc = float(weight) / (float(height)**2)
# Under 18.5 = underweight; 18.5 - 25 =  normal weight; 25 - 30 overweight; 30 - 35 = obese; 35+ clinically obese
if bmi_calc < 18.5:
    print(f"Your BMI is {round(bmi_calc, 1)}, you are underweight.")
elif bmi_calc < 25:
    print(f"Your BMI is {round(bmi_calc, 1)}, you are normal weight.")
elif bmi_calc < 30:
    print(f"Your BMI is {round(bmi_calc, 1)}, you are overweight")
elif bmi_calc < 35:
    print(f"Your BMI is {round(bmi_calc, 1)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi_calc, 1)}, you are clinically obese.")


# Coding Exercise 3.3: Leap Year
year = int(input("Which year do you want to check? "))
# divisible by 4 with no remainder is a leap year;
# EXCEPT every year that is divisible by 100
# UNLESS the year is also divisible by 400
# --- Personal Answer ---
if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a Leap Year")
elif year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
# --- Guides answer ---
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is not a Leap Year")
    else:
        print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")


# Coding Exercise 3.4: Pizza Order Practice
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L | ")
add_pepperoni = input("Do you want pepperoni? Y or N | ")
extra_cheese = input("Do you want extra cheese? Y or N | ")
# --- Guides answer ---
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is : ${bill}")


# Coding Exercise 3.5: Love Calculator
print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Count the number of times the letters (T, R, U, and E) occur in both your names for the first digit
# Count the number of times the letters (L, O, V, and E) occur in both your names for the second digit
# Hint:
# 1. lower() function changes all the letters in a string to lower case
# 2. count() function gives you the number of times a lett occurs in a string

lower_name1 = name1.lower()
first_dig = lower_name1.count("t")
first_dig += lower_name1.count("r")
first_dig += lower_name1.count("u")
first_dig += lower_name1.count("e")
lower_name2 = name2.lower()
first_dig += lower_name2.count("t")
first_dig += lower_name2.count("r")
first_dig += lower_name2.count("u")
first_dig += lower_name2.count("e")
print(first_dig)

lower_name1 = name1.lower()
second_dig = lower_name1.count("l")
second_dig += lower_name1.count("o")
second_dig += lower_name1.count("v")
second_dig += lower_name1.count("e")
lower_name2 = name2.lower()
second_dig += lower_name2.count("l")
second_dig += lower_name2.count("o")
second_dig += lower_name2.count("v")
second_dig += lower_name2.count("e")
print(second_dig)

love_score_raw = str(first_dig) + str(second_dig)
love_score = int(love_score_raw)

if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}.")

# --- Guides answer ---
combined_string = name1 + name2
lower_combined = combined_string.lower()
t = lower_combined.count("t")
r = lower_combined.count("r")
u = lower_combined.count("u")
e = lower_combined.count("e")
true = t + r + u + e
l = lower_combined.count("l")
o = lower_combined.count("o")
v = lower_combined.count("v")
e = lower_combined.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))


# Coding Project 3.A: Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

cross_road = input(print(
    "You're at a cross road. Where do you want to go ? Type 'left' or 'right'."))
if cross_road.lower() == "left":
    lake_boat = input(print(
        "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across the lake."))
    if lake_boat.lower() == "wait":
        door = input(print(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?."))
        if door.lower() == "yellow":
            print("Congratulations, you found the lost treasure on Treasure Island !!")
        if door.lower() == "red":
            print("You find a single rose in the middle of the room on a table. You pick up the rose with excitement only to find the rose has poisoned you. You fall into a deep slumber only to be awaken by a 'True Loves Kiss'. Game over.")
        else:
            print("A room full of glass shards riddles the floor. You scan the room to find a small chest tucked in the right corner of the room. Eagerly approaching the chest, you accidentally cut yourself on the shards and immediately go into Anaphylactic Shock. Game Over.")
    else:
        print("A shark falls in loves with you and drags you to the bottom of the ocean. Game Over.")
else:
    print("You begin walking on a yellow brick road to the Emerald City, forfeiting Treasure Island. Game Over.")
