
# Attributes y Methods
class Building:
    def __init__(self, floors, name, apartments):
        self.floors = floors
        self.name = name
        self.apartments = apartments

    def calculateHabitants(self):
        print ("Working calculateHabitants")

# DB Operations
class BuildingDB:
    def __init__(self, build):
        self.floors = build.floors
        self.name = build.name
        self.apartments = build.apartments

    def saveBuilding(self):
        print ("Working saveBuilding", self.name)
    
    def deleteBuilding(self):
        print ("Working deleteBuilding", self.name)

#Test
edificio = Building(10, "Bacata", 40)
BuildingDB(edificio).saveBuilding()
BuildingDB(edificio).deleteBuilding()
