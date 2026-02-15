class employee:
    salary = 320
    increment = 20
    @property
    def incrementSalary(self):
        return (self.salary + self.salary *(self.increment/100))
    
    @incrementSalary.setter               # kitna increment hua wo batane ke liye
    def incrementSalary(self,salary):
        self.increment = ((salary/self.salary)-1)*100



e = employee()
print(e.incrementSalary )
e.incrementSalary = 384.0
print(e.increment)