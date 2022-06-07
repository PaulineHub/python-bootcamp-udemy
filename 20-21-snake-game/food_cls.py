from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self. shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        random_x = randint(0, 280)
        random_y = randint(0, 280)
        self.goto(random_x, random_y)
        
