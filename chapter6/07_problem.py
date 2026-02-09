n=int(input("Enter a number"))
for i in range(1,n+1):
    if(i==1 or i==n): # i is row number 
     print("*"*n)
    else:                # Middle row
        print("*",end="")
        print(" "* (n-2),end="")
        print("*",end="")
        print("")

    