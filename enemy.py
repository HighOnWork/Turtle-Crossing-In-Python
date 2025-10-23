from turtle import Turtle
import random

class enemy_cars(Turtle):
    def __init__(self, Y_POSITION):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.Y_POSITION = Y_POSITION
    def color_of_car(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        if r == 255 and g == 255 and b == 255:
            self.color_of_car()
        color = (r, g, b)
        return color
    def location_of_cars(self):
        # Y_POSITION = random.randint(-280, 250)
        X_POSITION = random.randint(300, 1500)
        self.goto(X_POSITION, self.Y_POSITION)
    def move_car(self, SPEED_OF_CAR):
        random_speed_for_car = random.uniform(0, SPEED_OF_CAR)
        self.forward(-random_speed_for_car)
    def go_back(self):
        self.location_of_cars()
