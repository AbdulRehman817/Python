class Car:
    def __init__(self,name):
       self.name=name    
       
     


class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"
    
class Electric_Car(Engine,Battery,Car):
    pass


my_car=Electric_Car("Corolla")
print(my_car.battery_info())
print(my_car.name)
