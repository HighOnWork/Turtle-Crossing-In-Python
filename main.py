import turtle
from Game_Screen import GameScreen
from GameScore import my_score
from MyWalkingTurtle import walking_player

MOVE_SPEED = 20

turtle_crossing_screen = GameScreen()
player = walking_player(MOVE_SPEED)
scored_points = my_score()


turtle_crossing_screen.My_Game_Screen.onkeypress(key="w", fun=player.move_turtle)

while True:
    turtle_crossing_screen.My_Game_Screen.update()
    if player.ycor() >= 250:
        player.goto(0, -280)
    print(player.pos())

turtle.mainloop()