############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def direction_start_play():
  direction = input("Do you want to play a game of Blackjack ? y/n : ")
  if direction == 'y':
    return True
  else:
    return False

def direction_add_card():
  print(f"Your cards: {user_hand}, current score: {user_score}")
  print(f"Computer first card {computer_hand[0]}")
  is_adding_card = input("Type 'y' to get another card, 'n' to pass: ")
  if is_adding_card == 'y':
    return True
  else:
    return False

#first user's direction to play
is_playing = direction_start_play()

#Game running
while is_playing:
  is_starting_from_top = True
  while is_starting_from_top:
    clear()
    print(logo)
    game_over = False
    computer_hand = random.choices(cards, k=2)
    computer_score = sum(computer_hand)
    user_hand = random.choices(cards, k=2)
    user_score = sum(user_hand)
    is_adding_card = direction_add_card()
    #add a card
    while is_adding_card:
      user_hand.append(random.choice(cards))
      user_score = sum(user_hand)
      if user_score > 21:
        print("You went over. You loose 😭")
        is_playing = direction_start_play()
        game_over = True
        is_adding_card = False
      else:
        is_adding_card = direction_add_card()
    if not is_adding_card and not game_over:
      is_starting_from_top = False
  #annonce final scores
  print(f"Your final hand: {user_hand}, final score: {user_score}")
  print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
  if computer_score > user_score:
    print("You loose 😤")
  elif computer_score < user_score:
     print("You win 😁")
  elif computer_score == 21 and len(computer_hand) == 2:
    print("Lose, opponent has Blackjack 😱")
  elif user_score == 21 and len(user_hand) == 2:
    print("Win with a Blackjack 😎")
  else:
    print("Draw 🙃")
  #ask user if want to play again
  is_playing = direction_start_play()