class number:
    a = 1
    @classmethod
    def num(cls):
        print(cls.a)


n = number()
n.a = 45           #output is 1 after using classmethod 
n.num()