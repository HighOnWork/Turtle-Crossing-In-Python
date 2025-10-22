from turtle import Turtle
import random
import time

class enemy_cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.first_x_value = self.xcor()
        self.second_x_value = self.first_x_value - 20
        self.first_y_value = self.ycor()
        self.second_y_value = self.first_y_value - 10
    def color_of_car(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        if r == 255 and g == 255 and b == 255:
            self.color_of_car()
        color = (r, g, b)
        return color
    def location_of_cars(self):
        Y_POSITION = random.randint(-280, 250)
        self.goto(280, Y_POSITION)
    def move_car(self):
        random_speed_for_car = random.randint(0, 10)
        self.forward(-random_speed_for_car)
        time.sleep(0.01)
