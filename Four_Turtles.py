import turtle
a = turtle.Turtle()
a.speed(0)
a.shape("circle")
a.color("red")
b = turtle.Turtle()
b.speed(0)
b.shape("circle")
b.color("green")
c = turtle.Turtle()
c.speed(0)
c.shape("circle")
c.color("Cyan")
d = turtle.Turtle()
d.speed(0)
d.shape("circle")
d.color("yellow")

a.seth(0)
a.penup()
a.fd(200)
a.pendown()
a.left(181)


b.penup()
b.seth(90)
b.fd(200)
b.pendown()
b.left(181)

c.penup()
c.seth(181)
c.fd(200)
c.pendown()
c.left(181)

d.penup()
d.seth(270)
d.fd(200)
d.pendown()
d.left(181)


for i in range(90):
    a.fd(400)
    a.left(181)
    b.fd(400)
    b.left(181)
    c.fd(400)
    c.left(181)
    d.fd(400)
    d.left(181)









turtle.done()