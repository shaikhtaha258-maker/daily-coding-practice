class Number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):           # __add__(self, other)
        return self.n + num.n        # __sub__(self, other)
                                    # __mul__(self, other)
n = Number(2)
m = Number(2)

print(n + m)


'''In Python, we can define how operators like
 +, -, and == behave for our own custom class objects.'''