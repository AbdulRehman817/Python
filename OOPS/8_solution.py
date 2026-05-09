class Car:

    def __init__(self,name):
       self.__name=name   
        
    @staticmethod
    def car_description():
        return "Cars are used for transportation"
    @property         
    def name(self):
        return self.__name
     
class Electric_Car(Car):
    def __init__(self, __name, brand,power):
        super().__init__(__name, brand)
        self.power=power;
    
    
my_car=Car("Corolla")

print(my_car.name)


