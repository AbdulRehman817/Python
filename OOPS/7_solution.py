class Car:

    def __init__(self,name,brand):
       self.name=name   
        
    @staticmethod
    def car_description():
        return "Cars are used for transportation"
     
class Electric_Car(Car):
    def __init__(self, name, brand,power):
        super().__init__(name, brand)
        self.power=power;
    
    
my_car=Car("Corolla","Honda")
Car("Corolla","Honda")
print(my_car.car_description())
print(Car.car_description())


