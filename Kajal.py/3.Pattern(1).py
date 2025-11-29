import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Turtle Graphics")

# Create the turtle pen
pen = turtle.Turtle()
pen.speed(0)  # Set speed to the fastest
pen.width(2)  # Set line width

# Define the colors seen in the image
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

# Draw the spiral
# We loop 360 times to create the density of lines seen in the image
for x in range(360):
    # Select color based on the iteration number using standard Python modulo
    pen.pencolor(colors[x % 6])
    
    # Move the turtle forward by the current iteration value (x)
    # This makes the spiral grow outwards
    pen.forward(x)
    
    # Turn left by 59 degrees
    # 60 degrees would make a perfect hexagon. 
    # Using 59 creates the twisting spiral effect.
    pen.left(59)

# Keep the window open until clicked
turtle.done()