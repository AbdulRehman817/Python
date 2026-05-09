class Car:
    def __init__(self,name,brand):
        self.name=name
        self.__brand=brand
    # def full_name(self):
    #     return f"{self.name} {self.brand}"
    def get_brand(self):
        return self.__brand
    
    def set_brand(self,newbrand):
        self.__brand=newbrand
    
class Electric_Car(Car):
    def __init__(self, name, brand,power):
        super().__init__(name, brand)
        self.power=power;
    
my_car=Car("Corolla","Honda")
# print(my_car.name)
# print(my_car.brand)
# print(my_car.full_name())
print(my_car.get_brand())

my_car.set_brand("Suzuki")
print(my_car.get_brand())
