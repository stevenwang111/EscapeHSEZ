import tkinter as tk

def on_button_click(direction):
    print(f"You clicked {direction} button")

root = tk.Tk()
root.title("Direction Buttons")

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
