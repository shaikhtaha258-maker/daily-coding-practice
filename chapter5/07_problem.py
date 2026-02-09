post = input("Enter your post:")

#if("Taha" in post or "taha" in post ):     #<---|
if("Taha".lower() in post.lower()):         #<---| same as above
    print("This post is talking about Taha")
else:
    print("This post is not talking about Taha")