from turtle import Turtle

STARTING_POSITIONS = [(350, 0), (350, -20), (350, -40), (350, -60)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:

    def __init__(self):
        self.segments = []
        self.create_paddle()
        self.top_paddle = self.segments[0]
        self.bottom_paddle = self.segments[len(self.segments) - 1]

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white", "white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self, direction):
        if direction == "up":
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.top_paddle.forward(MOVE_DISTANCE)
        elif direction == "down":
            for seg_num in range(0, len(self.segments) - 1):
                new_x = self.segments[seg_num + 1].xcor()
                new_y = self.segments[seg_num + 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.bottom_paddle.forward(MOVE_DISTANCE)

    def up(self):
        self.top_paddle.setheading(UP)
        self.move("up")


    def down(self):
        self.bottom_paddle.setheading(DOWN)
        self.move("down")

