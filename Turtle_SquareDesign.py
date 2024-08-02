import turtle as t
t.penup()
t.setpos(-100,-100)
t.pendown()
def square(l):
    i=0
    col=["red","green","blue","purple","black","gold"]
    while(i<=22):
        t.speed(99999)
        t.color(col[i%6])
        t.begin_fill()
        for n in range(4):
            t.forward(l)
            t.left(91)
        t.end_fill()
        i+=1
    
square(200)
t.penup()
t.setpos(100,0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(100)
t.end_fill()
t.mainloop()