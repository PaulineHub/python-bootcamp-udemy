from replit import clear
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")
register_bid = 'yes'
bids = {}

#register bids
while register_bid == 'yes':
  name = input("What is your name ? ")
  bid = int(input("What's your bid ? "))
  bids[name] = bid
  register_bid = input("Are they any other biders ? Type 'yes' or 'no' : ")
  clear()
  
#compare bids
higher_bid = 0
for bid in bids:
  if bids[bid] > higher_bid:
    winner_name = bid
    higher_bid = bids[bid]

print(f"The winner is {winner_name} with a bid of {higher_bid} !")