from turtle import Turtle
import random

class enemy_cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
    def color_of_car(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        if r == 0 and g == 0 and b == 0:
            self.color_of_car()
        color = (r, g, b)
        return color
