#MONEY REMINDER
#penny = 0.01
#nickel = 0.05
#dime = 0.1
#quarter = 0.25

#VARIABLES
logo = """
              __    __                                     _      _              
  __   ___   / _|  / _|  ___   ___     _ __    __ _   __  | |_   (_)  _ _    ___ 
 / _| / _ \ |  _| |  _| / -_) / -_)   | '  \  / _` | / _| | ' \  | | | ' \  / -_)
 \__| \___/ |_|   |_|   \___| \___|   |_|_|_| \__,_| \__| |_||_| |_| |_||_| \___|
                                                                                                                                                                    
"""

coffee = """
      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'  
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_on = True
profit = 0

#FUNCTIONS
def check_ingredients(drink):
  """Check if there's enough ingredients in the ressources. Return boolean."""
  order_ingredients = MENU[drink]["ingredients"]
  missing_resource = False
  for ingredient in order_ingredients:
    if resources[ingredient] < order_ingredients[ingredient]:
      missing_resource = True
      print(f"Sorry there is not enough {ingredient}")
  return missing_resource

def calcul_money(quarters, dimes, nickels, pennies):
  """Calculate the amount of money given."""
  total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
  return total

def check_money(drink):
  """Check if the amount paid is enough. Return boolen if the drink is paid or not."""
  quarters_inserted = int(input("How many quarters ? : "))
  dimes_inserted = int(input("How many dimes ? : "))
  nickels_inserted = int(input("How many nickels ? : "))
  pennies_inserted = int(input("How many pennies ? : "))
  amount_paid = calcul_money(quarters_inserted, dimes_inserted, nickels_inserted, pennies_inserted)
  if amount_paid < MENU[drink]["cost"]:
    print("Sorry that's not enough money. Money refounded.")
    drink_paid = False
  else:
    change = amount_paid - MENU[drink]["cost"]
    print(f"Here is {change} in change.")
    drink_paid = True
  return drink_paid

def use_ressources(drink):
  """Susbtract ingredients used for the drink to the ressources."""
  order_ingredients = MENU[drink]["ingredients"]
  for ingredient in order_ingredients:
    resources[ingredient] -= order_ingredients[ingredient]

#MACHINE WORKING
print(logo)

while machine_on:
  prepare_order = True
  while prepare_order:
    order = input("What would you like ? (espresso/latte/cappuccino) ").lower()
    if order == "espresso" or order == "latte" or order == "cappuccino":
      missing_ingredient = check_ingredients(order)
      if missing_ingredient: 
        prepare_order = False
      else:
        print("Please insert coins.")
        enough_money = check_money(order)
        if not enough_money:
          prepare_order = False
        else:
          use_ressources(order)
          profit += MENU[order]["cost"]
          print(f"Here is your {order} ☕. Enjoy !")
          print(coffee)
    elif order == "report":
      for resource in resources:
        print(f"{resource} : {resources[resource]}")
      print(f"Profit : {profit}")
      prepare_order = False
    elif order == "off":
      machine_on = False
      prepare_order = False
      