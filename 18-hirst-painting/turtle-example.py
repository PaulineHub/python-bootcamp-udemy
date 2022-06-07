#from turtle import Turtle, Screen
import turtle as t
import random
""" 
tim = Turtle()
tim.shape("turtle") 
"""

# Square challenge
""" 
for _ in range(4):
    tim.fd(50)
    tim.right(90)
"""

# Dot challenge
""" 
for _ in range(10):
    tim.pendown()
    tim.fd(10)
    tim.penup()
    tim.fd(10) 
"""

# geometric shape challenge

""" 
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.pendown()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.fd(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
 """

#Random walk challenge
""" 
tim = t.Turtle()
t.colormode(255)
 """
"""
def random_color():
    for i in range(10):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
    return random_color

directions = ["right", "left"]

tim.width(8)
tim.speed(3)
tim.hideturtle()
tim.pendown()

for _ in range(50):
    tim.color(random_color())
    if random.choice(directions) == "right":
        tim.right(90)
    else:
        tim.left(90)
    tim.fd(20) 
"""

# Spirograph Challenge

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.hideturtle()
tim.width(2)


def random_color():
    for i in range(10):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
