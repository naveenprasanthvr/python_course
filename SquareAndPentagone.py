import turtle as t
t.speed(10)

'''def square(s):
    col = ["red","green","blue","yellow"]
    t.begin_fill()
    if s<=10:
        return
    else:
        
        for i in range(4):
            
            t.color(col[i%4])
            t.fd(s)
            square(s/2)
            t.left(90)
            t.end_fill()
        
        
        
        
square(100)
t.done()'''

def pen(s):
    
    col = ["red","green","blue","cyan","orange"]
    if s<=10:
        return
    else:
        for i in range(5):
            t.begin_fill()
            t.color(col[i%5])
            
            t.forward(s)
            pen(s/5)
            t.left(72)
            t.end_fill()
#t.end_fill()

pen(100)
t.done()










