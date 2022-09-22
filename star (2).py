
from random import *
from turtle import *

def star(height, colour):

    left_angle = 72
    right_angle = 144
    line_size = height * 0.409

    setheading(-left_angle)
    color(colour)
    pendown()
    begin_fill()
    segment_numbers = range(5)

    for seg_no in segment_numbers:
        forward(line_size)
        left(left_angle)
        forward(line_size)
        right(right_angle)

    end_fill()
    penup()

# star(100, 'purple')
star_count = input("Please enter number of stars to draw: ")
star_count = int(star_count)
speed("fastest")
setup(800, 800)
bgcolor("purple")

for star_num in range(star_count):
    x_pos = randint(-400, 400)
    y_pos = randint(-400, 400)

    size = randint(5, 20)
    colour = choice(['aquamarine', 'beige','bisque','blue', 'burlywood', 'coral','cornsilk','cyan', 'firebrick', 'gold', 
    'honeydew', 'ivory', 'khaki', 'lavender'])

    goto(x_pos, y_pos)

    star(size, colour)