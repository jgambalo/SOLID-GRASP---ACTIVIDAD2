import abc
from abc import ABC, abstractmethod

# Specific Interfaces
class iAnimal(ABC):
    @abc.abstractmethod
    def eat(self):
        pass

class iFlyAnimal(ABC):
    @abc.abstractmethod
    def fly(self):
        pass

class iWalkAnimal(ABC):
    @abc.abstractmethod
    def walk(self):
        pass

# Animals Classes      
class bird(iAnimal, iFlyAnimal):
    @classmethod
    def eat(self):
        print("Eat")

    @classmethod
    def fly(self):
        print("Fly")

class feline(iAnimal,iWalkAnimal):
    @classmethod
    def eat(self):
        print("Eat")

    @classmethod
    def walk(self):
        print("Walk")


#Test
print("---Dove---")
dove = bird()
dove.eat()
dove.fly()
print("---Tiger---")
tiger = feline()
tiger.eat()
tiger.walk()

