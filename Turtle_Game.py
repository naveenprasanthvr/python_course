import turtle, random

#BackGround
turtle.title("Turtle Race")
turtle.bgcolor("cornsilk")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.setpos(-200,200)
t.pendown()
#RangeLines
for i in range(1,11):
    t.write(i)
    t.seth(-90)
    t.forward(300)
    t.bk(300)
    t.seth(0)
    t.penup()
    t.forward(50)
    t.pendown()
    if i == 10:
        t.write("FINISH",font=('arial',20))
        
finishline = 250    #FinishLine

t.penup()
t.setpos(-200,-250)
t.pendown()
t.write("BY NAVEEN",font=('script',30,))

#CreatingNumberofPlayers
def create_player(colour,xpos,ypos):
    player = turtle.Turtle()
    player.penup()
    player.shape('turtle')
    player.color(colour)
    player.setpos(xpos,ypos)
    return player
    
p1 = create_player('green',-250,150)
p2 = create_player('blue',-250,100)
p3 = create_player('red',-250,50)
p4 = create_player('black',-250,0)
p5 = create_player('brown',-250,-50)

#ForwardMotion
while(1):
    p1.forward(random.randint(1,5))
    if p1.pos()[0]>=finishline:
        p1.write("  Winner Winner\n  Chicken Dinner!",font=('courier',10))
        break
    p2.forward(random.randint(1,5))
    if p2.pos()[0]>=finishline:
        p2.write("  Winner Winner\n  Chicken Dinner!",font=('courier',10))
        break
    p3.forward(random.randint(1,5))
    if p3.pos()[0]>=finishline:
        p3.write("  Winner Winner\n  Chicken Dinner!",font=('courier',10))
        break
    p4.forward(random.randint(1,5))
    if p4.pos()[0]>=finishline:
        p4.write("  Winner Winner\n  Chicken Dinner!",font=('courier',10))
        break
    p5.forward(random.randint(1,5))
    if p5.pos()[0]>=finishline:
        p5.write("  Winner Winner\n  Chicken Dinner!",font=('courier',10))
        break
    
turtle.done()