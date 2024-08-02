import turtle as t
i=0
color = ["green","blue","black","brown","red"]
while(i<=360):
    t.hideturtle()
    t.speed(99100)
    t.color(color[i%5])
    #t.begin_fill()
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(1)
    #t.end_fill()
    i+=1
t.exitonclick()