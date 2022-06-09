from turtle import Screen
from field_cls import Field
from paddle_cls import Paddle

# parameters of the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# create field, paddle, ball
field = Field()
paddle_player = Paddle()

# direct paddle's movements
screen.listen()
screen.onkey(paddle_player.up, "Up")
screen.onkey(paddle_player.down, "Down")

# play
game_is_on = True
while game_is_on:
    screen.update()
    #time.sleep(0.1)



# exit the screen
screen.exitonclick()
