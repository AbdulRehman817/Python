class Car:
    total_car=0;
    def __init__(self,name,brand):
       self.name=name    
       Car.total_car+=1
     
class Electric_Car(Car):
    def __init__(self, name, brand,power):
        super().__init__(name, brand)
        self.power=power;
    
    
Corolla=Car("Corolla","Honda")
Safari=Car("Safari","Honda")

print(Car.total_car)