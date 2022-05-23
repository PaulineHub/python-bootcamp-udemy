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

#Write your code below this line 👇
import random
options = [rock, paper, scissors]

#gamer and computer's choices
gamer_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n") 
gamer_choice = int(gamer_choice) 
print("you choice :", options[gamer_choice])
computer_choice = random.randint(0,2)
print("computer's choice :", options[computer_choice])

#rules
if gamer_choice >=0 and gamer_choice <= 2:
  if gamer_choice == computer_choice:
    print("null")
  elif (gamer_choice == 1 and computer_choice == 0) or (gamer_choice == 2 and computer_choice == 1) or (gamer_choice == 0 and computer_choice == 2):
    print("you win")
  else:
    print("you loose")
else:
  print("invalid number")