import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

# import colorgram
# colors = colorgram.extract('image.jpg',100)
# color_palette = []
# for i in range(len(colors)):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     new_color = (r, g, b)
#     color_palette.append(new_color)
# print(color_palette)

turtle.colormode(255)
tim.penup()
tim.hideturtle()

#Colors extracted
color_list = [(239, 136, 38), (217, 234, 244), (251, 247, 249), (24, 44, 72), (249, 238, 81), (121, 166, 186), (243, 112, 123), (6, 81, 165), (59, 112, 93), (179, 94, 49), (171, 152, 49), (201, 63, 156), (227, 235, 2), (126, 202, 64), (245, 93, 82), (39, 46, 45), (40, 40, 39), (174, 67, 137), (24, 64, 116), (227, 174, 168), (228, 169, 181), (115, 146, 115), (173, 192, 214), (180, 206, 172), (102, 127, 161), (177, 198, 203), (50, 73, 65), (50, 48, 49), (107, 134, 140)]
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1,number_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
