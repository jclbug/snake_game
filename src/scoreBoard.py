import turtle as scoreTim
import os

home = os.path.expanduser("~")
data_file_path = os.path.join(home, "snake_game_highscore.txt")


class ScoreBoard:
    def __init__(self):
        if not os.path.exists(data_file_path):
            with open(data_file_path, "w") as file:
                file.write("0")
        with open(data_file_path, "r") as file:
            self.highestScore = int(file.read())
        self.score = 0
        self.score_turtle = scoreTim.Turtle()

    def createScoreBoard(self, score, title, coord):
        self.score_turtle.color("white")
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.goto(coord[0], coord[1])
        self.score_turtle.write(f"{title} {score}", align="center", font=("Arial", 14, ))

    def updateScore(self):
        self.score += 1
        self.score_turtle.clear()
        self.createScoreBoard(self.score, "Score: ", [-250, 270])
        if (self.score < self.highestScore):
            self.createScoreBoard(self.highestScore, "Highest Score: ", [200, 270])
        else:
            self.createScoreBoard(self.score, "Highest Score: ", [200, 270])
            with open(data_file_path, "w") as file:
                file.write(f"{self.score}")
        


        