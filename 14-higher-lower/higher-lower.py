#IMPORTS
from game_data import data 
from art import logo
from art import vs
import random 
from replit import clear

#FUNCTIONS
def item_to_compare():
  """generate random item from data"""
  i = random.randint(0,len(data) - 1)
  return data[i]

def ask_question(item1,item2):
  """print the question on screen"""
  print(logo)
  print(f"Compare A : {item1['name']}, a {item1['description']}, from {item1['country']}.")
  print(vs)
  print(f"Against B : {item2['name']}, a {item2['description']}, from {item2['country']}.")
  guess = input("Who has more followers ? Type A or B : ")
  return guess

def result_more_followers(item1,item2):
  """give the answer of the question"""
  if item1['follower_count'] > item2['follower_count']:
    return 'a'
  else:
    return 'b'

#GLOBAL VARIABLES
game_over = False
score = 0
elt1 = item_to_compare()

#GAME
while not game_over:  
  elt2 = item_to_compare()
  #prevent bug 2 items identicals
  while elt1 == elt2:
    elt2 = item_to_compare()
  #ask question
  user_guess = ask_question(elt1,elt2).lower()
  #if right answer
  if user_guess == result_more_followers(elt1,elt2):
    score += 1
    clear()
    elt1 = elt2
  #if wrong answer
  else:
    print(f"Game over. Score : {score}")
    game_over = True

  
