import turtle

global angel_1
angel_1=0

def Square(x,y,size,color,angel):
    global angel_1
    turtle.pendown ()
    turtle.color (color)
    turtle.penup ()
    turtle.setx ( x )
    turtle.sety ( y )
    turtle.begin_fill ()
    turtle.pendown ( )
    turtle.right(angel-angel_1)
    angel_1= angel_1+angel
    turtle.forward (size)
    turtle.right(90)
    turtle.forward ( size )
    turtle.right (90)
    turtle.forward ( size )
    turtle.right (90)
    turtle.forward ( size )
    turtle.end_fill ()
    if (angel_1 >= 360):
        angel_1 = angel_1 - 360

def Parallelogram(x,y,size,color,angel):
    global angel_1
    turtle.pendown ()
    turtle.color (color)
    turtle.penup ()
    turtle.setx ( x )
    turtle.sety ( y )
    turtle.begin_fill ()
    turtle.pendown ( )
    turtle.right(angel-angel_1)
    angel_1 = angel_1+ angel
    turtle.forward (size)
    turtle.right(60)
    turtle.forward ( size )
    turtle.right (120)
    turtle.forward ( size )
    turtle.right ( 60 )
    turtle.forward ( size )
    turtle.end_fill ()
    if (angel_1 >= 360):
        angel_1 = angel_1 - 360

def Triangle(x,y,size,color,angel):
    global angel_1
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(angel-angel_1)
    angel_1 = angel_1 + angel
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()
    if (angel_1>=360):
        angel_1=angel_1-360


turtle.mainloop()