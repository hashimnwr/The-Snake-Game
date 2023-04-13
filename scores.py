from turtle import Turtle

FONT = ('arial', 15, 'normal')
ALIGNMENT = 'center'


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', 'w') as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()
