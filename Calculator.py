import time as t
import math
print ("CALCULATOR")
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
def per(a,b):
    c=a*b/100
    return c
def sqrt(a):
    c=math.sqrt(a)
    return c
while(1):
    e=input("Do you Want to CONTINUE or EXIT the Calculator: ")
    if(e=="exit"or e=="EXIT"):
        print("You Choosed to Exit")
        break
    elif(e=="continue"or e=="CONTINUE"):
        print("You Choosed to Continue")
        pass

    t.sleep(2)
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVITION")
    print("5.PERCENTAGE")
    print("6.SQUARE ROOT")
    z=input("Enter Your Choice From 1 to 7: ")
    
    if(z=='1'):
        x=float(input("Enter the first number: "))
        y=float(input("Enter the second number: "))
        print(x,"+",y,"is",add(x,y))
    elif(z=='2'):
        x=float(input("Enter the first number: "))
        y=float(input("Enter the second number: "))
        print(x,"-",y,"is",sub(x,y))
    elif(z=='3'):
        x=float(input("Enter the first number: "))
        y=float(input("Enter the second number: "))
        print(x,"x",y,"is",mul(x,y))
    elif(z=='4'):
        x=float(input("Enter the first number: "))
        y=float(input("Enter the second number: "))
        print(x,"/",y,"is",div(x,y))
    elif(z=='5'):
        x=float(input("Enter the first number: "))
        y=float(input("Enter the second number: "))
        print(x,"%",y,"is",per(x,y))
    elif(z=='6'):
        x=float(input("Enter the number to be square rooted: "))
        print("Square Root of ",x,"is",sqrt(x))        

        
   
    
    
    