from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.pencolor("Red")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"{self.score_player_1}    {self.score_player_2}", False, "center", ("Arial", 30, "normal"))

    def point_player_1(self):
        self.score_player_1 += 1
        self.update_scoreboard()
    def point_player_2(self):
        self.score_player_2 += 1
        self.update_scoreboard()

    def winner(self):
        self.clear()
        self.goto(0, 0)
        if self.score_player_1 > self.score_player_2:
            self.write(f"player 1 won", False, "center", ("Arial", 30, "normal"))
        else:
            self.write(f"player 2 won", False, "center", ("Arial", 30, "normal"))




