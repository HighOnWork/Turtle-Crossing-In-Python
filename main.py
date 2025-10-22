import turtle
import random
from Game_Screen import GameScreen
from GameScore import my_score
from MyWalkingTurtle import walking_player
from enemy import enemy_cars
import time
MOVE_SPEED = 20

num_of_turtles = None

enemy = []
turtle_crossing_screen = GameScreen()
player = walking_player(MOVE_SPEED)
scored_points = my_score()

turtle_crossing_screen.My_Game_Screen.onkeypress(key="w", fun=player.move_turtle)

def make_turtles():
    global enemy
    global num_of_turtles
    num_of_turtles = random.randint(1, 10)
    for i in range(0, num_of_turtles):
        new_car = enemy_cars()
        new_car.location_of_cars()
        enemy.append(new_car)
        enemy[i].color(enemy[i].color_of_car())

make_turtles() 

while True:
    turtle_crossing_screen.My_Game_Screen.update()
    for i in range(0, num_of_turtles):
        enemy[i].move_car()
        if abs(player.xcor() - enemy[i].xcor()) < 20 and abs(player.ycor() - enemy[i].ycor()) < 20:
            print("HIT")
    make_turtles()
    time.sleep(0.01)
    scored_points.give_score()
    if player.ycor() >= 250:
        scored_points.score_increase()
        player.goto(0, -280)
        
    

turtle.mainloop()