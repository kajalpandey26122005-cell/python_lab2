import turtle

def draw_spiral_squares():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(width=800, height=800)
    screen.title("Spiral of Squares")

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(1)
    pen.color("black")

    side_length = 15
    rotation_step = 5
    scale_increment = 0.9

    for _ in range(120):
        for _ in range(4):
            pen.forward(side_length)
            pen.left(90)
        pen.right(rotation_step)
        side_length += scale_increment

    screen.mainloop()

if __name__ == "__main__":
    draw_spiral_squares()