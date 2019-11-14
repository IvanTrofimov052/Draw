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
    if (angel > angel_1):
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

#tree
Square(-600, -200, 30, '#6e5614', 0)
Triangle(-720, -200, 205, 'green', 45)
Triangle(-675, -70, 150, 'green', 315)

# Bat
Square(600, -200, 100, 'black', 0)
Triangle(650, -250, 200, 'black', 45)
Triangle(370, -250, 200, 'black', 315)

# Square
Square(600, 148, 100, 'black', 0)
Square(500, 148, 100, 'blue', 0)
Square(700, 148, 100, 'yellow', 0)
Square(500, 148, 100, 'silver', 270)

#home
Square(-600, 200, 200, '#6e5614', 0)
Triangle(-840, 400, 205, 'red', 226)
Square(-725, 275, 50, 'blue', 1)

turtle.mainloop()
