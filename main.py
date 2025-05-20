from snake import Snake

import turtle as t
import tkinter as tk

import time
import utils

root = tk.Tk()
snake = Snake()

root.withdraw()

screen = t.Screen()
snake.startGame()

screen_width = screen.window_width() // 2
screen_height = screen.window_height() // 2

while(True):
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.food_collision()

    head = snake.getHead()
    x, y = head.xcor(), head.ycor()
    if x > screen_width - 10 or x < -screen_width + 10 or y > screen_height - 10 or y < -screen_height + 10:
        utils.promptPlayAgain(t, snake)
    snake.self_collision(t)

# screen.exitonclick()

