import turtle

def Square(x,y,size,color,angel):
    #Do(Гоша)
    print()
def Triangle(x,y,size,color,angel):
    #Do(Егор)
    print()
def Parallelogram(x,y,size,color,angel):
    turtle.pendown ()
    turtle.color (color)
    turtle.penup ()
    turtle.setx ( x )
    turtle.sety ( y )
    turtle.begin_fill ()
    turtle.pendown ( )
    turtle.right(angel)
    turtle.forward (size)
    turtle.right(60)
    turtle.forward ( size )
    turtle.right (120)
    turtle.forward ( size )
    turtle.right ( 60 )
    turtle.forward ( size )
    turtle.end_fill ()
Parallelogram(100,100,100,'green',90)
turtle.mainloop()
