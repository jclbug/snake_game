from tkinter import messagebox

def promptPlayAgain(turtle, snakeObject):    
    answer = messagebox.askyesno("Game Over", "Do you want to play again?")
    if answer:
        turtle.clearscreen()
        snakeObject.startGame()
    else: 
        exit()