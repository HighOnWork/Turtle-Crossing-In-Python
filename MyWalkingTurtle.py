from turtle import Turtle

class walking_player(Turtle):
    def __init__(self, move_speed):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(0, -280)
        self.turtle_speed = move_speed
    def move_turtle(self):
        self.forward(self.turtle_speed)
        