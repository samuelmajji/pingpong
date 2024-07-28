from turtle import Screen
from box import Box
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
box = Box()
scoreboard = Scoreboard()
screen.bgcolor("black")
screen.setup(1220,620)
screen.title("welcome to PingPong")
screen.tracer(0)
box.set_up()
box.draw_ground()
screen.update()
game_on = 1

screen.listen()
screen.onkey(box.move_up_r, "Up")
screen.onkey(box.move_down_r, "Down")
screen.onkey(box.move_up_l, "w")
screen.onkey(box.move_down_l, "s")

ball = Ball()
# ball.set_position()
while game_on:
    screen.update()
    time.sleep(0.000001)
    ball.ball_move()
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.new_position()
    for i in range(0, 3):
        if ball.distance(box.box_1[i]) < 20:
            angle = ball.heading()
            ball.setheading(540-angle)
        if ball.distance(box.box_2[i]) < 20:
            angle = ball.heading()
            ball.setheading(540-angle)

    if ball.xcor() > 595 or ball.xcor() < -595:
        if ball.xcor() < 0:
            ball.new_ball()
            scoreboard.point_player_2()
        elif ball.xcor() > 0:
            ball.new_ball()
            scoreboard.point_player_1()

    if scoreboard.score_player_2 == 5 or scoreboard.score_player_1 == 5:
        if scoreboard.score_player_2 == 5:
            scoreboard.winner()
        if scoreboard.score_player_1 == 5:
            scoreboard.winner()
        game_on = 0









screen.exitonclick()



