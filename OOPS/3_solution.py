# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.


class Car:
    def __init__(self,model,name):
        self.model=model
        self.name=name
    def full_name(self):
        return f"{self.model} {self.name}"
     

class Electric_Car(Car):
    def __init__(self,model,name,battery_size):
        super().__init__(model,name)
        self.battery_size=battery_size

my_tesla=Electric_Car("Tesla","Safari","80KWH")
print(my_tesla.full_name())