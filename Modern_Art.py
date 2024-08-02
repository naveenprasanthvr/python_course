import turtle as t
import random as r
t.bgcolor("sky blue")
t.speed(0)
def rand(o,p):
    i = 0
    t.color(o,p)
    t.begin_fill()
    while(i<=100):
        t.fd(r.randint(0,100))
        t.lt(90)
        t.fd(r.randint(0,100))
        t.rt(270)
        i+=1
    t.end_fill()
    t.setpos(0,0)
rand("blue","cyan")
rand("black","silver")
rand("green","red")
rand("brown","cornsilk2")
rand("grey","gold")

t.exitonclick()
t.done()