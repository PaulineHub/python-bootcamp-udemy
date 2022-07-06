from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.left(90)
        self.goto(random.choice(range(-310, 410)),
                  random.choice(range(-250, 310)))
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())
        if self.xcor() < -320:
            self.goto(320, self.ycor())

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
