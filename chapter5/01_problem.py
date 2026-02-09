a =int(input("Enter first number"))
b =int(input("Enter second number"))
c =int(input("Enter third number"))
d =int(input("Enter forth number"))
if(a>b and a>c and a>d):
   print("first number is greater")
elif(b>a and b>c and b>d):
   print("second number is greater")
elif(c>b and c>a and c>d):
   print("Third number is greater")
elif(d>a and d>b and d>c):
   print("fourth number is greater")