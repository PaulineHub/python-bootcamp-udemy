from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 250)
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def inscrease(self):
        self.level += 1
        self.clear()
        self.update()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
