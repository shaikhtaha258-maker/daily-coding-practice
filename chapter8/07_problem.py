with open("log.txt") as f:
    lines=f.readlines()
    
lineno=1
for line in lines:
    if("python" in line):
        print("python word present in line no",lineno)
        break
    lineno+=1
else:
    print("no python")    