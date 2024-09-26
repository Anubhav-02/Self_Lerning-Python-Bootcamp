# Day 4 Project - Rock Paper Scissor Game

import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

Rock ='''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)'''

Paper ='''
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)'''

Scissor ='''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.'''

your_choice = [Rock, Paper, Scissor]
computer_choice =[Rock, Paper, Scissor]

user_input = int(input("Enter 0, 1, or 2: "))
y = your_choice[user_input]  # Get the user's choice based on input
c = random.choice(computer_choice)  # Random choice for the computer

print(f'Your Choice is {y}')
print(f'Computer Choice is {c}')

if y == c:
    print("Draw")
elif (y == Rock and c == Scissor) or (y == Paper and c == Rock) or (y == Scissor and c == Paper):
    print("You win!")
else:
    print("You lose!")