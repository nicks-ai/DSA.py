import turtle

def draw_donut(turtle, radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_donut_hole(turtle, radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_donuts():
    window = turtle.Screen()
    window.bgcolor("white")

    donut_turtle = turtle.Turtle()
    donut_turtle.speed(0)

    colors = ["pink", "blue", "yellow", "green", "purple"]

    for i in range(5):
        donut_turtle.penup()
        donut_turtle.goto(i * 100 - 200, 0)
        donut_turtle.pendown()
        draw_donut(donut_turtle, 50, colors[i])
        draw_donut_hole(donut_turtle, 20, "white")

    window.mainloop()

draw_donuts()