'''class employee:
    salary=10000
    def Salary(self):
        print(self.salary)


    
s=employee()
s.salary=-50000
s.Salary() '''

class employee:
    def __init__(self,salary):
        self._salary=salary

    @property        # @property → method ko variable jaisa use karne ke liye
    def salary(self):
        return self._salary

    
    @salary.setter  # @setter → value set karne se pehle check/validate karne ke liye
    def salary(self,value):
        if value<10000:
            print("salary is not less than 10000")
        else:
            self._salary=value
            
s = employee(10000)
s.salary=-5000.  
print(s.salary)        