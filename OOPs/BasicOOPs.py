class vehicle:
    # shared variable
    attr = "4 Wheeler"

    #CTOR
    def __init__(self, make):
        self.make = make    #self.make public variable

    def drive(self):
        print(f"{self.make} vehicle is driving")

class car(vehicle):
    def __init__(self, make, model):
        super().__init__(make)  # calling parent class CTOR : vehicle.__init__(make)
        self.__model = model    # self.__model private variable
    
    def drive(self):
        print(f"{self.make} {self.__model} car is driving")

class truck(vehicle):
    def __init__(self, make, model):
        super().__init__(make)  # calling parent class CTOR : vehicle.__init__(make)
        self.__model = model    # self.__model private variable
    
    def drive(self):
        print(f"{self.make} {self.__model} truck is driving")

MyVehicle = vehicle("Generic")
MyCar = car("BMW","X5")
Mytruck = truck("Volvo","Roadline")

MyVehicle.drive()
MyCar.drive()
Mytruck.drive()

print("vehicle category : ", car.attr) # accessing shared variable using class name
print("vehicle category : ", Mytruck.attr) # accessing shared variable using object
