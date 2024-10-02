import turtle
import random
import os

# 获取backgrounds文件夹中的所有图片文件名
background_folder = "backgrounds"
background_files = [f for f in os.listdir(background_folder) if f.endswith(".png")]

# 随机选择一张图片
selected_background = random.choice(background_files)

# 设置turtle画布的背景图片
screen = turtle.Screen()
screen.bgpic(os.path.join(background_folder, selected_background))

# 保持窗口打开，直到用户关闭它
turtle.done()
