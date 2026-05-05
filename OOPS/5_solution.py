class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"
class Electric_Car(Car):
    def __init__(self,power,brand,model):
        super().__init__(brand,model)
        self.power=power

my_car=Electric_Car("75kwh","Corolla","Toyota")
print(my_car.power)