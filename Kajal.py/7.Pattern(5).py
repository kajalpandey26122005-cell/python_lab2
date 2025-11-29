import math
import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Rose Curve (Rhodonea Curve)")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing speed
pen.color("purple")
pen.pensize(2)

# Parameters for the rose curve
a = 100  # Scaling factor (adjust for size)
k = 5    # Number of petals (if k is odd, petals = k; if even, petals = 2k)

# Draw the rose curve
pen.penup()
pen.goto(0, 0)
pen.pendown()

for theta in range(0, 360 * k + 1, 1):  # Loop through angles
    # Convert degrees to radians
    theta_rad = math.radians(theta)

    # Rose curve equation: r = a * sin(k * theta)
    r = a * math.sin(k * theta_rad)

    # Convert polar to Cartesian coordinates
    x = r * math.cos(theta_rad)
    y = r * math.sin(theta_rad)

    # Move the turtle to the calculated position
    pen.goto(x, y)

# Hide the turtle and display
pen.hideturtle()
turtle.done()