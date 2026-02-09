with open("poem.txt") as f:
    content=f.read()
    if("Twinkle" in content):
        print("The word twinkle pesent in the content")
    else:
        print("The word twinkle is not present in the content")
