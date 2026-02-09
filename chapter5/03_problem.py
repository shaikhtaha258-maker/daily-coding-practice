p1 ="Make a lot of money"
p2 ="Buy now"
p3 ="Subscribe this"
p4 ="click this"

c=input("Type your comments")
if((p1 in c) or (p2 in c) or (p3 in c) or (p4 in c)):
    print("Comment is spam")
else:
    print("Comment is not spam")