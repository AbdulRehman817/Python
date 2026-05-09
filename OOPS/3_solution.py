# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.


class Car:
    def __init__(self,name,model):
        self.name=name;
        self.model=model
        
    def full_name(self):
        return f"{self.name} {self.model}"
    
class Electric_Car(Car):
  def __init__(self,battery_size,brand,model):
      super().__init__(brand,model)
      self.battery_size=battery_size;
      
my_car=Electric_Car("Corolla","2019","210kwh")

print(my_car.battery_size)
print(my_car.name)