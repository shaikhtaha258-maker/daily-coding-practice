f=open("file.text")
data=f.read()
print(data)
f.close()

# The same can be written using with statement like this
with open("file.text") as f:
    print(f.read())

# you dont have to explicitly close the file   