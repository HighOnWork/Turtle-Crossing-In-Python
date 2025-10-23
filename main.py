import turtle
import random
from Game_Screen import GameScreen
from GameScore import my_score
from MyWalkingTurtle import walking_player
from enemy import enemy_cars
import time

SPEED_OF_MY_CAR = 5
MOVE_SPEED = 30
y_pos = -250
time_to_sleep = 0.01
num_of_turtles = None

enemy = []
turtle_crossing_screen = GameScreen()
player = walking_player(MOVE_SPEED)
scored_points = my_score()

turtle_crossing_screen.My_Game_Screen.onkeypress(key="w", fun=player.move_turtle)

def make_turtles():
    global y_pos
    global SPEED_OF_MY_CAR
    global enemy
    global num_of_turtles
    for i in range(0, 20):
        new_car = enemy_cars(Y_POSITION=y_pos)
        new_car.location_of_cars()
        new_car.color(new_car.color_of_car())
        enemy.append(new_car)
        y_pos += 25
        
make_turtles()

while True:
    turtle_crossing_screen.My_Game_Screen.update()
    for i in range(0, 20):
        enemy[i].move_car(SPEED_OF_MY_CAR)
        if enemy[i].xcor() <= -280:
            enemy[i].go_back()
        if abs(player.xcor() - enemy[i].xcor()) < 20 and abs(player.ycor() - enemy[i].ycor()) < 20:
            break
    time.sleep(time_to_sleep)
    scored_points.give_score()
    if player.ycor() >= 250:
        scored_points.score_increase()
        player.goto(0, -280)
        for i in range(0, 20):
            enemy[i].location_of_cars()
            time_to_sleep *= 0.9
    
turtle.mainloop()