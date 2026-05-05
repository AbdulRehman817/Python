#  Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    def full_name(self):
        return f'{self.brand} {self.model}'
    
    def get_brand(self):
       return self.__brand+"!"
    
class Electric_Car(Car):
    def __init__(self,size,model,brand):
     super().__init__(model,brand)
     self.size=size

my_car=Electric_Car("19kwh",'Corolla',"Toyota")
print(my_car.get_brand())