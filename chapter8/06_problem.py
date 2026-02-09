with open("log.txt") as f:
    content=f.read()
if("python" in content):
    print("Python word present in log.txt")
else:
    print("Python word is not present in log.txt")
