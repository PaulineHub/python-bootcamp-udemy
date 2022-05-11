import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
end_of_game = False
life_points = 6
chosen_word = random.choice(word_list)
display = []

for letter in chosen_word:
  display.append("_")

#Testing code
print(chosen_word)

while not end_of_game:
  guess = input("Chose a letter.\n").lower()
  i = 0
  letter_founded = False
  for letter in chosen_word:
    if letter == guess:
      letter_founded = True
      display[i] = guess
    i += 1
  if letter_founded:
    print(display)
    letter_founded = False
  else:
    life_points -= 1
    print(f"life points: {life_points}")
    print(stages[life_points + 1])
  if "_" not in display:
    end_of_game = True
    print("you won !")
  if life_points == 0:
    end_of_game = True
    print("Game over")
