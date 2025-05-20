import turtle as tim
import food 
import scoreBoard
import utils

class Snake:
    new_food = food.Food()
    def __init__(self):
        self.turtles = []
        self.initialCoord = (0, 0), (-10, 0), (-20, 0)
        self.score = None
        self.snake_food = None
        self.screen = tim.Screen()

    def snake_direction(self, setMoveDirection, checkDirection):
        if(int(self.turtles[0].heading()) != checkDirection):
            self.turtles[0].setheading(setMoveDirection)

    def snakePart(self):
        new_turtle = tim.Turtle("square")
        new_turtle.color("white")
        new_turtle.shapesize(0.7,0.7)
        new_turtle.penup()
        return new_turtle
    
    def createSnake(self, position):
        new_turtle = self.snakePart()
        new_turtle.goto(position[0], position[1])
        self.turtles.append(new_turtle)

    def initialSnake(self):
        for i in range(3):
            self.createSnake(self.initialCoord[i])

    def getHead(self):
        return self.turtles[0]

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            x_axis = self.turtles[i-1].xcor()
            y_axis = self.turtles[i-1].ycor()
            self.turtles[i].goto(x_axis, y_axis)
        self.turtles[0].forward(10)

    def self_collision(self, turtle):
        head = self.getHead()
        for i in range(6, len(self.turtles)-1):
            if (head.distance(self.turtles[i]) < 10):
                utils.promptPlayAgain(turtle, self)
                        
    def moveUp(self):
        self.snake_direction(90, 270)

    def moveDown(self):
        self.snake_direction(270, 90)
        
    def moveLeft(self):
        self.snake_direction(180, 0)

    def moveRight(self):
        self.snake_direction(0, 180)

    def extendSnake(self):
        new_part = self.snakePart()
        last_snake = self.turtles[len(self.turtles) - 1]
        x_coor = last_snake.xcor()
        y_coor = last_snake.ycor()
        new_part.goto(x_coor, y_coor)
        self.turtles.append(new_part)

    def food_collision(self):
        if (self.getHead().distance(self.snake_food) < 10):
            self.new_food.foodRefresh(self.snake_food)
            self.score.updateScore()
            self.extendSnake()

    def startGame(self):
        self.turtles = []
        self.snake_food = self.new_food.createFood()
        self.screen.setup(width=600, height=600)
        self.initialSnake()
        self.screen.title("Python Game using Python")
        self.score = scoreBoard.ScoreBoard()
        self.score.createScoreBoard()
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        
        self.screen.onkey(self.moveUp, "Up")
        self.screen.onkey(self.moveDown, "Down")
        self.screen.onkey(self.moveLeft, "Left")
        self.screen.onkey(self.moveRight, "Right")
        self.screen.listen()


