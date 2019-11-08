import turtle

global angel_1
angel_1 = 0
turtle.speed(100000)


def Square(x, y, size, color, angel):
    global angel_1
    turtle.pendown()
    turtle.color(color)
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.begin_fill()
    turtle.pendown()
    if(angel > angel_1):
        turtle.right(angel - angel_1)
    else:
        turtle.right(angel_1 - angel)
    angel_1 = angel
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()


def Parallelogram(x, y, size, color, angel):
    global angel_1
    turtle.pendown()
    turtle.color(color)
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.begin_fill()
    turtle.pendown()
    if (angel > angel_1):
        turtle.right(angel - angel_1)
    else:
        turtle.right(angel_1 - angel)
    angel_1 = angel
    turtle.forward(size)
    turtle.right(60)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(60)
    turtle.forward(size)
    turtle.end_fill()


def Triangle(x, y, size, color, angel):
    global angel_1
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.pendown()
    if (angel > angel_1):
        turtle.right(angel - angel_1)
    else:
        turtle.right(angel_1 - angel)
    angel_1 = angel
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()

Square(600, -200, 100, 'black', 0)
Triangle(650, -250, 200, 'black', 45)
Triangle(370, -250, 200, 'black', 315)

turtle.mainloop()
