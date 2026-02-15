class Animal:
    pass

class pets(Animal):
     pass

class Dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow")
       
d = Dog()
d.bark()        

