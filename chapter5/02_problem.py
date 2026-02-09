s1 =int(input("Enter marks of SFL:"))
s2 =int(input("Enter marks of CN:"))
s3 =int(input("Enter marks of OOP:"))
parcent = ((s1+s2+s3)/300)*100
if(parcent>=40 and s1>33 and s2>33 and s3>33):  #<--- at least 33 marks in single subject
    print("Congrats you are pass")
    print("parcentage is:",parcent)
else:
    print("Fail")