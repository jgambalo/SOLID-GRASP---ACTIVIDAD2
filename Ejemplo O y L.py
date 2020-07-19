import abc
from abc import ABC, abstractmethod

# Abstract Class
class City(ABC):
    @abc.abstractproperty
    def population(self):
        return 0
        
#Extended Classes
class newYork(City):
    @property
    def population(self):
        return 18000

class LA(City):
    @property
    def population(self):
        return 5000

class Dallas(City):
    @property
    def population(self):
        return 1000


#Test
cityArray = []

cityArray.append (newYork())
cityArray.append (LA())
cityArray.append (Dallas())

for obj in cityArray: 
    print(obj.population)