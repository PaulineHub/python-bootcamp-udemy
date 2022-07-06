from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__() 
        self.score = 0
        with open("data.txt") as data:  
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def inscrease(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    """ def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT) """
        
