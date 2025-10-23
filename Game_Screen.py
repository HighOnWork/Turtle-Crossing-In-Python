from turtle import Screen

class GameScreen():
    def __init__(self):
        self.My_Game_Screen = Screen()
        self.My_Game_Screen.colormode(255)
        self.My_Game_Screen.tracer(0)
        self.My_Game_Screen.setup(600, 600)
        self.My_Game_Screen.listen()
    