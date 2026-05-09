class Car:
    def __init__(self,name,brand):
        self.name=name
        self.__brand=brand
    def fuel_type(self):
        return "petrol"    
class Electric_Car(Car):
    def __init__(self, name, brand,power):
        super().__init__(name, brand)
        self.power=power;
    def fuel_type(self):
        return "electric charge"    
    
my_car=Car("Corolla","Honda")
# print(my_car.name)
# print(my_car.brand)
# print(my_car.full_name())
print(my_car.fuel_type())
