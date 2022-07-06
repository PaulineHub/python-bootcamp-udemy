from turtle import Screen
from snake_cls import Snake
from food_cls import Food
from scoreboard_cls import Scoreboard
import time

# parameters of the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create a snake body and food
snake = Snake()
food = Food()
score = Scoreboard()

# direct snake's movements
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move the snake
game_is_on = True
while game_is_on:
    screen.update()  # !! needed when screen.tracer(0)
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.inscrease()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with any segment of the tail
    # excluding the head [0] of the array segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
        
# exit the screen
screen.exitonclick()
