class employee:            # Base class / Parent class
    company = "microsoft"
    def show(self):
        print("dream company is",self.company,"for all softaware engineeres")


class  programmer(employee):   #child class
    #company = "Google"
    def Dream(self):
        print("Most powerfull company in the world is",self.company)

a = employee()
b = programmer()



print(a.company,b.company)