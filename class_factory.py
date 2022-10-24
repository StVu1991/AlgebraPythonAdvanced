#vidjeti zašto ne radi
class Car:
    def factory(type):
        class Sedan(Car):
            def display(self):
                print("ssss")
                print(f"This is a new Sedan.")

        class Sports(Car):
            def display(self):
                print("ssss")
                print(f"This is a new Sports car.")

        if (str(type).lower() == "sedan"):
            print("fff")
            return Sedan()

        if (str(type).lower() == "sports"):
            print("fff")
            return Sports()


sedan = Car.factory("sedan")
sports = Car.factory("sports")