import turtle

# Set up the screen
s = turtle.Screen()
s.bgcolor("black")
s.title("Cool Shapes")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.width(2)

# List of colors
colors = ["red", "green", "blue", "orange", "purple", "cyan"]

# Draw the pattern
for i in range(360):
    t.color(colors[i % 6])
    t.forward(100)
    t.backward(100)
    t.right(45)
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(60)
    t.backward(60)
    t.right(1)
    t.forward(100)

t.hideturtle()
turtle.done()