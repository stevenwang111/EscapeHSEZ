import turtle

# 创建画布
screen = turtle.Screen()
screen.setup(1600, 900)

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

# 保持窗口打开，直到用户关闭它
turtle.done()
