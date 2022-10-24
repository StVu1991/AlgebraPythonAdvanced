class Car:
    axles = 2
    wheels = 4
    pass


car1 = Car()
car2 = Car()

print(car1.wheels)
print(car1.axles)
print(car2.wheels)
print(car2.axles)

car2.wheels = 6

print(car2.wheels)
print(car2.axles)
