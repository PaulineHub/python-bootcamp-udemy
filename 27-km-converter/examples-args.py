# Function with multiple arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    #print(sum)

add(1, 2, 3)

# Function with multiple keyword arguments
def calculate(n, **kwargs):
    #print(kwargs)  # return {'add': 3, 'mult': 4}
    n += kwargs["add"]
    n *= kwargs["mult"]
    #print(n) # return 20


calculate(2, add=3, mult=4)  

# Class with multiple keyword arguments
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Renauld", color="pink")
print(my_car.make)