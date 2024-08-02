import turtle as t
def cloud(radius,x,y):
    t.bgcolor("blue")
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.color("white")
    t.rt(90)

    for i in range(2):
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.lt(90)
    t.begin_fill()
    t.circle(radius,270)
    t.fd(radius*2)
    t.end_fill()
cloud(50,100,250)
