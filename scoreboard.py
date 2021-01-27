from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update()
    def update(self):
        self.write(f"score: {self.score}", align = "center", font = ("Arial", 22, "normal"))
    def increase(self):
        self.score += 1
        self.clear()
        self.update()
    def gameover(self):
        self.clear()
        self.write(f"game over. score:{self.score}", align = "center", font = ("Arial", 22, "normal"))
       
