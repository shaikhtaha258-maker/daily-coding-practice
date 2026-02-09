n=int(input("Enter a number"))
for i in range(1,n+1):
    print(" "*(n-i),end="")       #n change nahi hoga and i 1 se n tak jaiga
    print("*"*(2*i-1),end="")
    print("")

    