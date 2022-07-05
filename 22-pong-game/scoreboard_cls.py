from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Helvetica', 40, 'bold')

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.update()

    def update(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def inscrease(self):
        self.score += 1
        self.clear()
        self.update()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
