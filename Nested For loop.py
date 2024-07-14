for i in range(1,10):
    print()
    for j in range(1,i+1):
        if (j == 1):
            for k in range(j, 10-i):
                print(end=" ")        
        print(j, end="")    
