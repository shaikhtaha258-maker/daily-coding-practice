num = int(input("Enter number"))
for i in range(2,num):
    if(num % i)==0:
        print("Given number is not prime")
        break
    else:
        print("Given number is prime")