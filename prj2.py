import turtle

def Square(x,y,size,color,angel):
    #Do(Егор) коммитнулось проверка
    print()
#def Triangle(x,y,size,color,angel):
    #Do(Гоша) коммитнулось проверка
    #print()
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
   
def Triangle(x,y,size,color,angel):
    turtle.shape("turtle")
    turtle.pendown ()
    turtle.color (color)
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.fd(size)
    turtle.right(angel)
    turtle.fd(size)
    turtle.goto(x,y)
    turtle.end_fill()
    




Triangle(-200,200,300,"red",90)
turtle.mainloop()
