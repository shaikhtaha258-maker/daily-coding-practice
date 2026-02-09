a = int(input("Enter Your Age:"))  #if elif else ladder 
if(a>=18):
    print("You are eligible for voting")

elif(a<0):
    print("Negative & 0 is not available")
elif(a==0):
    print("0 is invalide")
else:
    print("You are not eligible for voting")

print("end program")