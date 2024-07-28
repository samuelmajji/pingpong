from turtle import Turtle
import random

angle = []
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.new_ball()

    def set_position(self):
        angle.append(random.randint(0, 70))
        angle.append(random.randint(110,250))
        angle.append(random.randint(290,340))
        angles = random.choice(angle)

        self.setheading(angles)

    def new_ball(self):
        self.goto(0, 0)
        self.set_position()

    def ball_move(self):
        self.forward(5)

    def new_position(self):
        angle = 360 - self.heading()
        self.setheading(angle)