from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time


# Setup Screen
screen = Screen()
width, height = 800, 600
screen.setup(width, height)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))
ball = Ball()

# Create movement controls
screen.listen()
screen.onkey(p1.up, "Up")
screen.onkey(p1.down, "Down")
screen.onkey(p2.up, "w")
screen.onkey(p2.down, "s")

# Game Loop
is_running = True

while is_running:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect wall collision
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect paddle collision
    if (ball.distance(p1) < 50 
        and ball.xcor() > 320
        or ball.distance(p2) < 50 
        and ball.xcor() < -320):
        ball.bounce_x()
    
    # Detect p1 miss
    if ball.xcor() < -380 :
        ball.reset()
        scoreboard.p2_point()

    # Detect p2 miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.p1_point()

screen.exitonclick()