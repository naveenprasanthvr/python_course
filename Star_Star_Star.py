import turtle as t
t.speed(10)
def star(s):
    if s<=10:
        return
    else:
        for i in range(5):
            t.fd(s)
            star(s/2)
            t.left(216)

star(200)
t.done()