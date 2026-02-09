a = int(input("Enter Your Age:"))

#if statement no:1
if(a%2==0):
    print("Even number")
#end of if statement no:1

#if statement no:2                                         
if(a>=18):
    print("You are eligible for voting")

elif(a<0):
    print("Negative is not available")
elif(a==0):
    print("0 is invalide")
else:
    print("You are not eligible for voting")
#end of if statement no:1

print("end program")