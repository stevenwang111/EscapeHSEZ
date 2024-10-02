import turtle
import tkinter as tk
import random
import os

def move_turtle(direction):
    if direction == "w":
        player.sety(t.ycor() + 100)
    elif direction == "s":
        player.sety(t.ycor() - 100)
    elif direction == "a":
        player.setx(t.xcor() - 100)
    elif direction == "d":
        player.setx(t.xcor() + 100)



#screen = turtle.Screen()
#t = turtle.Turtle()

#screen.listen()
#screen.onkey(lambda: move_turtle("w"), "w")
#screen.onkey(lambda: move_turtle("s"), "s")
#screen.onkey(lambda: move_turtle("a"), "a")
#screen.onkey(lambda: move_turtle("d"), "d")

#screen.mainloop()
screen = turtle.Screen()
screen.setup(1600, 900)

# 获取backgrounds文件夹中的所有图片文件名
background_folder = "backgrounds"
background_files = [f for f in os.listdir(background_folder) if f.endswith(".png")]

# 随机选择一张图片
selected_background = random.choice(background_files)

# 设置turtle画布的背景图片
#screen = turtle.Screen()
screen.bgpic(os.path.join(background_folder, selected_background))

# 保持窗口打开，直到用户关闭它
#turtle.done()



# 创建海龟对象
painter = turtle.Turtle()
painter.speed(0)  # 设置最快速度

# 画格子
for i in range(-8, 9):
    painter.penup()
    painter.goto(i*100, -450)
    painter.setheading(90)
    painter.pendown()
    painter.forward(900)

for j in range(-4, 5):
    painter.penup()
    painter.goto(-800, j * 100-50)
    painter.pendown()
    painter.setheading(0)
    painter.forward(1600)

# 隐藏海龟
painter.hideturtle()

root = tk.Tk()
root.title("控制器")

#canvas = tk.Canvas(root, width=400, height=400)
#canvas.pack()


player = turtle.RawTurtle(screen)
player.penup()
player.goto(50,0)

screen.listen()
screen.onkey(lambda: move_turtle("w"), "w")
screen.onkey(lambda: move_turtle("s"), "s")
screen.onkey(lambda: move_turtle("a"), "a")
screen.onkey(lambda: move_turtle("d"), "d")



frame = tk.Frame(root)
frame.pack()

up_button = tk.Button(frame, text="Up", command=lambda: move_turtle("w"))
up_button.grid(row=0, column=1)

down_button = tk.Button(frame, text="Down", command=lambda: move_turtle("s"))
down_button.grid(row=2, column=1)

left_button = tk.Button(frame, text="Left", command=lambda: move_turtle("a"))
left_button.grid(row=1, column=0)

right_button = tk.Button(frame, text="Right", command=lambda: move_turtle("d"))
right_button.grid(row=1, column=2)

root.mainloop()
