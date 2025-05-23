import turtle as tim
import random

class Food:

    def createFood(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)

        self.new_tim = tim.Turtle("circle")
        self.new_tim.color("#f03e3e")
        self.new_tim.shapesize(0.5, 0.5)
        self.new_tim.penup()
        self.new_tim.goto(rand_x, rand_y)
        return self.new_tim

    def foodRefresh(self, food):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        food.goto(rand_x, rand_y)

