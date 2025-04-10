from turtle import Turtle

with open('highscore.txt') as file:
    highscore = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}   HighScore: {highscore}", align="center")
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}   HighScore: {highscore}", align="center")

    def game_over(self):
        global highscore
        if self.score > int(highscore):
            highscore = self.score

        with open('highscore.txt', mode='w') as new_file:
            new_file.write(str(highscore))
        self.score = 0
        self.goto(0, 100)
        self.write(arg="Game Over!!!", align='center', font=('Arial', 40, 'bold'))
        self.hideturtle()
        self.goto(0, 75)
        self.write(arg=f"Final Score: {self.score}   HighScore: {highscore}", align='center', font=('Arial', 25, 'bold'))
        self.goto(0, 50)
        self.write(arg=f"Press R to restart", align='center', font=('Arial', 15, 'bold'))
