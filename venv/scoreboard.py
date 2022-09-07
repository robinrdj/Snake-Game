from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("data.txt") as data:
            self.highscore = int(data.read())

        self.penup()
        self.goto(0, 270)
        self.write(f"score:{self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score:{self.score} High Score:{self.highscore}", align="center", font=("Arial", 24, "normal"))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        with open("data.txt", mode="w") as data:
            data.write(f"{self.highscore}")



