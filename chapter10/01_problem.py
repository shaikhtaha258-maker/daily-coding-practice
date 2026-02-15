class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j   

    def show(self):
        print(f"2D vector is{self.i} + {self.j}")    


class threeDvector(twoDvector):
    def __init__(self, i, j,k):
        super().__init__(i, j) 
        self.k=k  
    def show(self):    
        print(f"2D vector is{self.i} + {self.j} + {self.k}")    
    

a = twoDvector(2,3)
a.show()
b = threeDvector(2,3,4)   
b.show() 