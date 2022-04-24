# import colorgram

# extract_colors = colorgram.extract(
#     'd:/15jlin/Documents/GitHub/100-Days-of-Python/Day-18-Turtle-GUI/dot.jpg', 30)
# # colors = colorgram.extract("dot.jpg", 6)


# rgb_colors = []
# for color in extract_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     rgb_colors.append((r, g, b))

# print(rgb_colors)

import random
from turtle import Turtle, Screen
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62),
              (47, 66, 82)]

# 10 x 10 spots
# 20 in size
# 50 apart
timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(1)
timmy.speed(10)
timmy.penup()
screen = Screen()
screen.colormode(255)

row_spots = 10
col_spots = 10
xcor = 0
ycor = 0
step = 50
for y in range(0, row_spots):
    for x in range(0, col_spots):
        timmy.goto(xcor, ycor)
        timmy.dot(20, random.choice(color_list))
        xcor += step
    ycor += step
    xcor = 0

screen.exitonclick()
