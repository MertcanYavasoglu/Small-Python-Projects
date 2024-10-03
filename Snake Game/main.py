from tkinter import *
import tkinter as tk
import random

# THIS CODE IS UNFINISHED 
# THIS CODE IS UNFINISHED 
# THIS CODE IS UNFINISHED 

window = Tk()
window.title("Snake")
window.minsize(1920, 1080)

canvas = tk.Canvas(window, width=1920, height=1080,)
canvas.configure(bg='black')
canvas.pack()

direction = 3  # 0-up  1-down  2-left  3-right
player = canvas.create_rectangle(600, 600, 630, 630, fill='green')
berry_x = random.randrange(0, 1890, 30)
berry_y = random.randrange(0,1050, 30)
berry = canvas.create_rectangle(berry_x, berry_y, berry_x+30, berry_y+30, fill='white')

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
    global berry
    global berry_x
    global berry_y
    coords_berry = canvas.coords(berry)
    coords_player = canvas.coords(player)
    base_x = 0
    base_y= 0
    moveable_limit_x_left = canvas.coords(berry)[0]
    moveable_limit_x_right = 1920 - canvas.coords(berry)[2]
    moveable_limit_y_down = 1080 - canvas.coords(berry)[3]
    moveable_limit_y_up = canvas.coords(berry)[1]
    if coords_berry == coords_player:
        list_x = moveable_limit_x_left, moveable_limit_x_right
        list_y = moveable_limit_y_down, moveable_limit_y_up
        choice_x = random.choice(list_x)
        choice_y = random.choice(list_y)
        if choice_x == moveable_limit_x_right:
            base_x = coords_berry[2]
        if choice_y == moveable_limit_y_down:
            base_y = coords_berry[3]

        berry_move_x = random.randrange(base_x, choice_x, 30)
        berry_move_y = random.randrange(base_y, choice_y, 30)
        canvas.move(berry, berry_move_x, berry_move_y)
    window.after(250, berry_spawn)

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
