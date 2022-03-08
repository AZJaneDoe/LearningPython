# #!/bin/python

# ################################################################################
# # Programmer: Allie
# # File: Day_4_Rock_Paper_Scissors.py
# Coding Exercise 4.1: Heads or Tails
# Coding Exercise 4.2: Banker Roulette
# Coding Project 4.A: Rock, Paper, Scissors
# # Subjects: Randomization and Python Lists
# # Date: March 2, 2022
# ################################################################################


# Randomization
# import random
# random_integer = random.randint(1, 10)
# print(random_integer)
# random_float = random.random()
# print(random_float)


# Coding Exercise 4.1: Heads or Tails
import random
coin = random.randint(0, 1)
if coin == 0:
    print("Heads!")
else:
    print("Tails!")

# Coding Exercise 4.2: Banker Roulette
names_string = input("Give me everbody's names, seperated by a comma. ")
names = names_string.split(", ")
random_payer = random.randint(0, len(names)-1)
loser = names[random_payer]
print(f"{loser} going to buy the meal today!")
# Coding Exercise 4.2: Banker Roulette [GUIDES ANSWER]
loser = random.choice(names)
print(f"{loser} going to buy the meal today!")

# Coding Project 4.A: Rock, Paper, Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand_types = [rock, paper, scissors]
hand_one = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
print(hand_types[hand_one])

computer = random.randint(0, 2)
computer_shape = hand_types[computer]
print(f"Computer chose: {computer_shape}")

if hand_one == 0 and computer == 1:
    print('You lose')
elif hand_one == 1 and computer == 2:
    print('You lose')
elif hand_one == 2 and computer == 0:
    print('You lose')
elif hand_one == 0 and computer == 2:
    print('You win')
elif hand_one == 1 and computer == 0:
    print('You win')
elif hand_one == 2 and computer == 1:
    print('You win')
elif hand_one == computer:
    print('It is a tie!')
else:
    print('You typed an invalid number, you lose!')
