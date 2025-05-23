import turtle as scoreTim

class ScoreBoard:
    def __init__(self):
        with open("snake_data.txt", "r") as file:
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
            with open("snake_data.txt", "w") as file:
                file.write(f"{self.score}")
        


        