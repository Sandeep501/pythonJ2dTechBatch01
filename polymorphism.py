# polymorphism | inheritence

class Animal(): # --> ParentClass
    def sound(self):
        return "Animal Sound"
        
class Dog(Animal):  # --> ChildClass
    
    def sound(self):
        return "Dog will bark"
    
    def typeOfAnimal(self):
        return "This is a 4 legged animal"

class Cat(Dog):
    
    def sound(self):
        return "Cat will Meow"
    
class Human(Animal):
    pass

CatInstance = Cat()
print(CatInstance.sound())
print(CatInstance.typeOfAnimal())
    