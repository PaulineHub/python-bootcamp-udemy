import time
from turtle import Screen
from player_cls import Player
from car_manager_cls import CarManager
from scoreboard_cls import Scoreboard

# Parameters of the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Create turtle, cars and scoreboard
player = Player()
cars = []
level = Scoreboard()

for car_index in range(0, 20):
    new_car = CarManager()
    cars.append(new_car)

turtle_alive = True

# Direct turtle's movements
screen.listen()
screen.onkey(player.up, "Up")

# Play
game_is_on = True
while game_is_on:
    # screen udpate every 0.1 seconds
    time.sleep(0.1)
    screen.update()
    
    # Move cars
    for car in cars:
        if turtle_alive:
            car.move()
            # Detect collision with car
            if player.distance(car) < 20:
                level.gameover()
                turtle_alive = False

    # Detect finishing line for the player
    if player.ycor() == player.finish_line:
        level.inscrease()
        player.start_from_bottom()
        for car in cars:
            car.increase_speed()
    