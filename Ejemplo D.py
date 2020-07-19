import abc
from abc import ABC, abstractmethod

# Connection Interface
class connection(ABC):
    @abc.abstractmethod
    def getData(self):
        pass

    @abc.abstractmethod
    def setData(self):
        pass

#DB Class
class DatabaseService(connection):

    @classmethod
    def getData(self):
        print("Getting Data From DB")

    @classmethod
    def setData(self):
        print("Setting Data From DB")

#API Class
class APIService(connection):

    @classmethod
    def getData(self):
        print("Getting Data From API")

    @classmethod
    def setData(self):
        print("Setting Data From API")


#Test
DB = DatabaseService()
DB.getData()
DB.setData()

API = APIService()
API.getData()
API.setData()

