import colorgram
import turtle as t
import random

tim = t.Turtle()    # instantiate a new turtle object called 'tim'
tim.shape('turtle')
t.colormode(255)
rgb_colors = []


def colors_from_image():
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        queue_color = (r, g, b)
        rgb_colors.append(queue_color)
    del rgb_colors[0:2]


colors_from_image()


def million_dollar_canvas(start):
    # Tim the turtle goes Faster
    tim.speed(0)
    for _ in range(10):
        tim.penup()             # don't draw when turtle moves
        tim.goto(-250, start)   # move the turtle to a location
        # Create the dots art
        for _ in range(10):
            tim.penup()
            tim.forward(50)
            tim.dot(20, random.choice(rgb_colors))
        start += 50

    # Draw the canvas frame.
    tim.goto(-250, -350)
    tim.pendown()
    tim.pensize(10)
    for _ in range(4):
        tim.fd(550)
        tim.left(90)
    tim.hideturtle()


million_dollar_canvas(-300)


screen = t.Screen()
screen.screensize(2500, 2500)
screen.exitonclick()