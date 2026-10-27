from turtle import *

def draw_coloful_square():
    speed(5)  # Painting speed control
    colors=["red", "orange", "yellow", "green", "blue", "purple"]
    for length in range(40, 320, 30):
        pencolor(colors[length//30 % len(colors)])
        for _ in range(4):
            forward(length)
            right(90)
        right(10)

draw_coloful_square()
done()







