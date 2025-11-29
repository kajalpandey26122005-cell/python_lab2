import turtle

# Set up the turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")

# Set turtle properties
t.color("red")
t.fillcolor("red")
t.pensize(3)
t.speed(5)

# Begin filling the shape
t.begin_fill()

# Draw the left curve of the heart
t.left(140)
t.forward(180)
t.circle(-90, 200)

# Draw the right curve of the heart
t.left(120)
t.circle(-90, 200)
t.forward(180)

# End filling the shape
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until clicked
screen.exitonclick()