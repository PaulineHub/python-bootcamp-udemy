from turtle import Turtle

class Field:

    def __init__(self):
        self.trace_line()

    def trace_line(self):
        line = Turtle("square")
        line.color("white", "white")
        line.penup()
        line.hideturtle()
        line.sety(300)
        line.setheading(270)
        line.pensize(5)
        for i in range(20):
            line.begin_fill()
            line.stamp()
            line.end_fill()
            line.forward(50)



