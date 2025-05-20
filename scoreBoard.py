import turtle as scoreTim

class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.score_turtle = scoreTim.Turtle()

    def createScoreBoard(self):
        self.score_turtle.color("white")
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.goto(-10, 270)
        self.score_turtle.write(f"| Score: {self.score} |", align="center", font=("Arial", 14, ))

    def updateScore(self):
        self.score += 1
        self.score_turtle.clear()
        self.createScoreBoard()
        