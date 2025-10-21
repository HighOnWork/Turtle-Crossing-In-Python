import turtle
from Game_Screen import GameScreen
from GameScore import my_score
from MyWalkingTurtle import walking_player
from enemy import enemy_cars

MOVE_SPEED = 20

cars = enemy_cars()
turtle_crossing_screen = GameScreen()
player = walking_player(MOVE_SPEED)
scored_points = my_score()

turtle_crossing_screen.My_Game_Screen.onkeypress(key="w", fun=player.move_turtle)

while True:
    turtle_crossing_screen.My_Game_Screen.update()
    cars.location_of_cars()
    cars.color(cars.color_of_car())
    scored_points.give_score()
    if player.ycor() >= 250:
        scored_points.score_increase()
        player.goto(0, -280)

turtle.mainloop()