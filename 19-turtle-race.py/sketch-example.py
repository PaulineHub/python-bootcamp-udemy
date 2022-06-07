from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# w = forwards
# s = backwards
# a = counter-clockwise
# d = clockwise
# c = clear drawing

def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear_drawing():
    tim.reset()

screen.listen()
#screen.onkey(key="w", fun=move_forwards)
screen.onkey(move_forwards, "w")
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
