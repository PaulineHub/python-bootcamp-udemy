#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

logo = """   
  / __| | | | __/ __/ __| |_   _| || | __| 
 | (_ | |_| | _|\__ \__ \   | | | __ | _|  
  \___|\___/|___|___/___/__ |_| |_||_|___| 
 | \| | | | |  \/  | _ ) __| _ \           
 | .` | |_| | |\/| | _ \ _||   /           
 |_|\_|\___/|_|  |_|___/___|_|_\           
                                    """


#Choosing a random number between 1 and 100.
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
print(f"Pssst, the correct answer is {answer}.") 
#Choosing level of difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
if difficulty == 'easy':
  attemps = 10
else:
  attemps = 5
#starting guessing
stop_game = False
while not stop_game:
  print(f"You have {attemps} attemps remaining to guess the number.")
  guess = int(input("Make a guess : "))
  if guess == answer:
    print(f"You got it ! The answer was {answer}.")
    stop_game = True
  else:
    attemps -= 1
    if attemps == 0:
      print(f"Game over. The answer was {answer}.")
      stop_game = True
    else:
      if guess > answer:
        print("Too higth.")
      else:
        print("Too low.")
      print("Guess again.")