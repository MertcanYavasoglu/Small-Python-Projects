from tkinter import *
import tkinter as tk
import random

# THIS CODE IS UNFINISHED 

window = Tk()
window.title("Snake")
window.minsize(1920, 1080)

canvas = tk.Canvas(window, width=1920, height=1080,)
canvas.configure(bg='black')
canvas.pack()

direction = 3  # 0-up  1-down  2-left  3-right
player = canvas.create_rectangle(0, 0, 30, 30, fill='green')

def move_up(event):
    global direction
    direction = 0

def move_down(event):
    global direction
    direction = 1

def move_left(event):
    global direction
    direction = 2

def move_right(event):
    global direction
    direction = 3

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

def check_coords():
    coords = canvas.coords(player)
    if (coords[0] < 0 or coords[2] > 1920 or coords[1] < 0 or coords[3] > 1080):
        return "boundary_collision"
    return "no_collision"

def berry_spawn():
    berry_x = random.randrange(0, 1890, 30)
    berry_y = random.randrange(0,1050, 30)
    berry = canvas.create_rectangle(berry_x, berry_y, berry_x+30, berry_y+30, fill='white')
    coords_berry = canvas.coords(berry)
    coords_player = canvas.coords(player)

def game_loop():
    collision_result = check_coords()

    if collision_result == "boundary_collision":
        quit()

    if direction == 0:
        canvas.move(player, 0, -30)
    elif direction == 1:
        canvas.move(player, 0, 30)
    elif direction == 2:
        canvas.move(player, -30, 0)
    elif direction == 3:
        canvas.move(player, 30, 0)
    
    window.after(250, game_loop)  # Schedule the game loop to run again after 1000ms (1 second)

# Start the game loop
game_loop()
berry_spawn()
window.mainloop()
