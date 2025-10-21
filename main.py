import turtle
from Game_Screen import GameScreen
from GameScore import my_score
from MyWalkingTurtle import walking_player

turtle_crossing_screen = GameScreen()
player = walking_player()
scored_points = my_score()

turtle_crossing_screen.My_Game_Screen.update()

turtle.mainloop()