import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
passwd = ""

for n in range(nr_letters):
  passwd += random.choice(letters)

for n in range(nr_symbols):
  passwd += random.choice(symbols)

for n in range(nr_numbers):
  passwd += random.choice(numbers)

print(f"Your password is {passwd}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwd_rand = []

for n in range(nr_letters):
  passwd_rand.append(random.choice(letters)) 

for n in range(nr_symbols):
  passwd_rand.append(random.choice(symbols))

for n in range(nr_numbers):
  passwd_rand.append(random.choice(numbers))

final_rand_pass = ""
random.shuffle(passwd_rand)
pass_len = len(passwd_rand)
for n in range(pass_len):
  final_rand_pass += passwd_rand[n]

print(f"Your random password is {final_rand_pass}")