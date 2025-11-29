import turtle
import math

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.hideturtle()

# Define the parameters for the flower-like shape
num_petals = 8
radius = 100
angle_step = 2 * math.pi / num_petals

# Define the colors for the petals
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white"]

# Draw the petals
for i in range(num_petals):
    # Calculate the angle for this petal
    angle = i * angle_step
    
    # Move to the starting position of the petal
    t.penup()
    t.goto(0, 0)
    t.setheading(angle * 180 / math.pi)
    t.forward(radius)
    t.pendown()
    
    # Draw the petal
    t.color(colors[i])
    t.begin_fill()
    for j in range(100):
        t.forward(2 * math.pi * radius / 100)
        t.left(360 / 100)
    t.end_fill()

# Keep the window open
turtle.done()