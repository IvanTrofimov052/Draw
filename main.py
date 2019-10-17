import turtle

def Square(x,y,size,color,angel):
    #Do(Егор) коммитнулось проверка
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
#Triangle(Гоша)
import turtle
from turtle import *
def Triangle(x,y,a,b,n,color,col,angel):
    turtle.shape("turtle")
    turtle.setx(x)
    turtle.sety(y)
    turtle.width(n)
    turtle.color(color,col)
    turtle.begin_fill()
    turtle.pendown()
    turtle.fd(a)
    turtle.right(angel)
    turtle.fd(b)
    turtle.goto(x,y)
    turtle.end_fill()
Triangle(-200,200,300,200,2,"red","blue",90)
turtle.mainloop()
