# Problem: Add a method to the Car class that displays the full name of the car (brand and model).


class Car:
    def __init__(self,model,name):
        self.model=model
        self.name=name
    def full_name(self):
        return f"{self.model} {self.name}"
     

my_car=Car("Toyota","Corolla")
print(my_car.full_name())