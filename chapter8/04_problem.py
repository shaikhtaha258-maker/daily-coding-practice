#st ="Donkey"
with open("file2.txt") as f:
    content=f.read()
    newcontent=content.replace("#####","Donkey")

with open("file2.txt","w") as f:
    f.write(newcontent)    
