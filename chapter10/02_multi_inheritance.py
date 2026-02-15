class employee:            
    company = "microsoft"
    def show(self):
        print("dream company is",self.company,"for all softaware engineeres")


class coder:
    language = "Python"
    def printlangua(self):
        print("Easy language for biggeners is:",self.language)        


class  programmer(employee,coder):  #child class 
    #company = "Google"
    def Dream(self):
        print("Most powerfull company in the world is",self.company,"and most trending language is:",self.language)

a = employee()
b = programmer()
c = coder()



b.Dream()