import turtle as t

# --- basic setup ---
t.bgcolor("#c6dcf3")          # light blue background (adjust as you like)
t.colormode(255)
t.speed(0)                    # fastest drawing
t.hideturtle()
t.pensize(2)
t.pencolor("#4b4f58")         # dark grey line color

# --- draw spiro-square pattern ---
def spiro_squares(side=200, turns=90, angle=5):
    for _ in range(turns):
        for _ in range(4):
            t.forward(side)
            t.left(90)
        t.left(angle)

spiro_squares(side=180, turns=90, angle=5)

# keep window open until clicked
t.done()