n=int(input("Enter a Number to be display as a Pyramid: "))
for i in range(1,n+1):        
    print(str(i)*i)
if (n<1):
    print("You Entered an Invalid Number, Please Enter a valid Number")