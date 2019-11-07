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
    turtle.right(angel - angel_1)
    angel_1 = angel_1 + angel
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()
    if (angel_1 >= 360):
        angel_1 = angel_1 - 360

def Parallelogram(x, y, size, color, angel):
    global angel_1
    turtle.pendown()
    turtle.color(color)
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(angel - angel_1)
    angel_1 = angel_1 + angel
    turtle.forward(size)
    turtle.right(60)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(60)
    turtle.forward(size)
    turtle.end_fill()
    if (angel_1 >= 360):
        angel_1 = angel_1 - 360

def Triangle(x, y, size, color, angel):
    global angel_1
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(angel - angel_1)
    angel_1 = angel_1 + angel
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()
    if (angel_1 >= 360):
        angel_1 = angel_1 - 360

Square(-100, -200, 200, 'green', 0)
Triangle(-133, -200, 190, 'red', 45)
Square(-50, -250, 100, 'black', 0)

Parallelogram(-100, 150, 200, '#800000', 75)
Parallelogram(-25, 195, 100, 'black', -120)
print(angel_1)

Square(600, -200, 100, 'black', 180)
Triangle(650, -250, 200, 'black', -135)
Triangle(370, -250, 200, 'black', 315)

Square(-500, -200, 30, '#5c3e0d', 45)
Triangle(-650, -210, 200, 'green', 360)
Triangle(-580, -100, 100, 'green', 315)


turtle.mainloop()