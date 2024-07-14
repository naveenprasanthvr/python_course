import math
print("CALCULATOR")

def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
def sqr(a,b):
    c=a**b
    return c
def sqrt(a):
    c=math.sqrt(a)
    return c
def decoration(ans, word):
    hypenLength = len(str(ans))
    hypenRightSide = "-" * hypenLength
    HeaderLength = len("----Your Answer is:"+ hypenRightSide)
    hypenFooter = "-"*HeaderLength
    
    print("----Your Answer is:"+hypenRightSide)
    print("\t",word, ans)
    print(hypenFooter,)

while(1):
    print("1.ADDITION")
    print("2.SUBTRAACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.SQUARE")
    print("6.SQUARE ROOT")
    print("7.EXIT")
    i = int(input("Enter Your Choice:"))
    if (i==1):
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        print(decoration(add(a,b),str(str(a)+" + "+str(b)+" =")))
    elif (i==2):
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        print(decoration(sub(a,b),str(str(a)+" - "+str(b)+" =")))
    elif (i==3):
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        print(decoration(mul(a,b),str(str(a)+" x "+str(b)+" =")))
    elif (i==4):
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        print(decoration(div(a,b),str(str(a)+" / "+str(b)+" =")))
    elif (i==5):
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        print(decoration(sqr(a,b),str(str(a)+" Power "+str(b)+" =")))
    elif (i==6):
        a=int(input("Enter the First Number:"))
        print(decoration(sqrt(a),"SQRT ="))
    elif (i==7):
        print("You Choosed to Exit Calculator")
        break
    else:
        print("Wrong Choice!")
        continue