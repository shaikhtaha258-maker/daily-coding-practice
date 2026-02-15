class employee:
    def __init__(self):
        print("Constructor of employee")
    
    a = 1

class programmer(employee):
    def __init__(self):
        #super().__init__()
        print("Constructor of programmer")
    b = 2

class manager(programmer):
    def __init__(self):
        super().__init__() 
        print("Constructor of manager")
    c = 3



#p = programmer() # Prints only programmer constructor
m = manager()      # prints both prog and manager constructor using super key
