import tkinter as tk
import turtle

def on_button_click(direction):
    if direction == "Up":
        t.sety(t.ycor() + 100)
    elif direction == "Down":
        t.sety(t.ycor() - 100)
    elif direction == "Left":
        t.setx(t.xcor() - 100)
    elif direction == "Right":
        t.setx(t.xcor() + 100)

root = tk.Tk()
root.title("Direction Buttons")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

screen = turtle.Screen()
t = turtle.RawTurtle(screen)

frame = tk.Frame(root)
frame.pack()

up_button = tk.Button(frame, text="Up", command=lambda: on_button_click("Up"))
up_button.grid(row=0, column=1)

down_button = tk.Button(frame, text="Down", command=lambda: on_button_click("Down"))
down_button.grid(row=2, column=1)

left_button = tk.Button(frame, text="Left", command=lambda: on_button_click("Left"))
left_button.grid(row=1, column=0)

right_button = tk.Button(frame, text="Right", command=lambda: on_button_click("Right"))
right_button.grid(row=1, column=2)

root.mainloop()
