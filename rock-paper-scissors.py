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


game = [rock,paper,scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

import random
computer = random.randint(0,2)

if computer == player:
  print(f"You chose:\n{game[player]}\nComputer chose:\n{game[computer]}\nDraw")
elif (computer == 0 and player == 1) or (computer == 1 and player == 2) or (computer == 2 and player == 0):
  print(f"You chose:\n{game[player]}\nComputer chose:\n{game[computer]}\nYou win")
elif (computer == 1 and player == 0) or (computer == 2 and player == 1) or (computer == 0 and player == 2):
  print(f"You chose:\n{game[player]}\nComputer chose:\n{game[computer]}\nYou lose")
else:
  print("You typed an invalid number, you lose!")
