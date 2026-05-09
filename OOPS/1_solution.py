# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.


class Car:
    def __init__(self,model,brand):
        self.model=model;
        self.brand=brand;
        
my_car=Car('2019','Corolla')
print(my_car.brand)
print(my_car.model)