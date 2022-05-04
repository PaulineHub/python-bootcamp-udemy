#COURS 2

#f-string : print(f"I'm {number} years old")
#converting data type : float(), int(), str()
#data type : type()
#round number with two decimal : round(number, 2)

#TIP CALCULATOR

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Questions
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill ?"))
percentage_tip = int(input("What percentage tip would you like to give ? 10, 12 or 15 ?"))
people = int(input("How many people to split the bill ?"))

#Calcul
bill_with_tip = bill + bill * (percentage_tip / 100)
bill_per_person = round(bill_with_tip / people, 2)
print(f"Each person should pay : {bill_per_person}$")