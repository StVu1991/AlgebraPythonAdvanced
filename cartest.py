__author__ = "Stjepan"

from cars import *

car1 = Car("Chevy", "Volt", 15000.00, 10)
sedan1 = Car("Ford", "Focus", 10000.00, 4)

car1.sellCar(3)
car1.display()
sedan1.doors = 3
sedan1.display()