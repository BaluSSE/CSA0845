# author balu
# greatest of three integers using loopin
a = input("enter value of a")
b = input("enter value of b")
c = input("enter value of c")
if(a>b):
    if(a>c): 
        print("the greatest",a)
    else:
        print("the greatest",c)
else:
        if (b>c):
            print("the greatest",b)
        else:
            print("the greatest",c)
