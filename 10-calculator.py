#LOGO
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

#FUNCTION CALCULATE
def calculate(n1, op, n2):
  if op == "+":
    return n1 + n2
  elif op == "-":
    return n1 - n2
  elif op == "*":
    return n1 * n2
  elif op == "/":
    return n1 / n2

continue_operation = True
#first input number
number1 = float(input("What the first number ? "))

#do operations until the user say no
while continue_operation:
    #rest of the inputs
    operator = input("+\n-\n*\n/\nPick an operation : ")
    number2 = float(input("What the next number ? "))
    #calculate result
    result = calculate(number1, operator, number2)
    #print result and ask continue or not the calcul
    print(f"{number1} {operator} {number2} = {result}")
    continue_operation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation : ")
    if continue_operation == 'n':
        continue_operation = False
    number1 = result