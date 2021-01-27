# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:12:05 2021

@author: liwaiho
"""
from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.title("snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.gameover()

    for s in snake.segment[1:]:
        if snake.head.distance(s) < 10:
            game_is_on = True
            scoreboard.gameover()
    
screen.exitonclick()
