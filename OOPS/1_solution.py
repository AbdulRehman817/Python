# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.


class Car:
    def __init__(self,model,name):
        self.model=model
        self.name=name

my_car=Car("Toyota","Corolla")
print(my_car.model)
print(my_car.name)