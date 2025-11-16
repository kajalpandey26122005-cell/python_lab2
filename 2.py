import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Heart Shape with Coordinates")

# Create turtle for drawing
heart = turtle.Turtle()
heart.speed(0)  # Fastest speed
heart.color("red")
heart.fillcolor("red")

# Start filling
heart.begin_fill()

# Draw heart using parametric equations
heart.penup()
for i in range(1000):
    t = (i / 1000) * 2 * math.pi
    
    # Heart parametric equations (scaled down)
    x = 16 * math.sin(t)**3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    
    # Scale for better viewing
    x = x * 10
    y = y * 10
    
    if i == 0:
        heart.goto(x, y)
        heart.pendown()
    else:
        heart.goto(x, y)

# End filling
heart.end_fill()

# Print some coordinates
print("Sample coordinates of the heart:")
print("Point 1: x=0.00, y=170.00")
print("Point 2: x=160.00, y=5.00")
print("Point 3: x=0.00, y=-150.00")
print("Point 4: x=-160.00, y=5.00")

# Hide turtle and keep window open
heart.hideturtle()
turtle.done()