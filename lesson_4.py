from typing import Any


class ElectroCar:
    def __init__(self, power,battery):
        self.power = power
        self.battery = battery
    def info(self):
        print(f"мощность {self.power} Vat\nзаряд батареи {self.battery} Mah")
    def add(self,a,b):
        print(a+b)
    
    def __repr__(self):# perp == print
        return f"мощность {self.power} Vat\nзаряд батареи {self.battery} Mah - это метод pepr"
    def __str__(self):#str == print
        return f"мощность {self.power} Vat\nзаряд батареи {self.battery} Mah - это мед str"
    # def __call__(self):
    #     print("hello")
    "магические методы для арифметических действий"
    
    def __add__(self, other): # add вызывается с помощью + как на 34 строчке кода показано
        new_power = self.power + other.power
        return ElectroCar(new_power, self.battery)
    def __sub__(self, other): # sub вызывается с помощью - как на 35 строчке кода показано
        new_power = self.power - other.power
        return ElectroCar(new_power, self.battery)
    def __mul__(self, other): #  mul вызывается с помощью * как на 36 строчке кода показано
        new_power = self.power * other.power
        return ElectroCar(new_power, self.battery)  
    def __truediv__(self, other): # truediv вызывается с помощью / как на 37 строчке кода показано
        new_power = self.power / other.power
        return ElectroCar(new_power, self.battery)
    def __div__(self, other): # div вызывается с помощью // как на 38 строчке кода показано
        new_power = self.power // other.power
        return ElectroCar(new_power, self.battery)
    
    
    "магические методы для оператов сравнения"
    def __gt__(self,other): # > ключ для вызова
        return self.battery > other.battery
    def __lt__(self,other): # < ключ для вызова
        return self.battery < other.battery
    def __eq__(self,other): # == ключ для вызова
        return self.battery == other.battery
    def __ne__(self,other): # != ключ для вызова
        return self.battery != other.battery
    def __ge__(self,other): # != ключ для вызова
        return self.battery >= other.battery
    def __le__(self,other): # != ключ для вызова
        return self.battery <= other.battery
car = ElectroCar(120, 20000)
car_2 = ElectroCar(120, 20000)
# car.info()
# car.add(1,2)
# print(car)
print(car+car_2)
# print(car-car_2)
# print(car*car_2)
# print(car/car_2)
# print(car//car_2)
# print(car>car_2)
# print(car<car_2)
# print(car==car_2)
# print(car!=car_2)
# print(car>=car_2)
# print(car<=car_2)
# print("hello")
# car()


        