"Инкапсуляция"

class Laptops:
    def __init__(self, monitor, keyboard, color):
        self.monitor = monitor # Публичный
        self._keyboard = keyboard # Зашишенный 
        self.__color = color # Приватным 

    @property 
    def color(self):
        return self.__color

    def info(self): # Публичный
        print(self.monitor, self._keyboard, self.__color)
        self.__private()


    def _protected(self): # Зашишенный
        print("Это защищенный метод") 

    def __private(self): # Приватным 
        print("Это приватный метод") 

    "@ - декоратор"
    @property 
    def private(self):
        return self.__private



macbook = Laptops(15.5, "С белой подсцветкой", "Белый")
huawei = Laptops(14.6, "С RGB подсцветкой", "Сырый")

# print(huawei.monitor, huawei._keyboard, huawei.color)
# print(macbook.monitor, macbook._keyboard, macbook.color)

macbook.info()
# huawei.info()

# macbook._protected() 
# huawei._protected() 

# macbook.private()
# huawei.private()



import time 

def say_hello(func): 
    def start(): 
        time.sleep(1) 
        print("Hello World!") 
        time.sleep(1)
        func()
        time.sleep(1)
        print("Bue!")
        time.sleep(1)
    return start


@say_hello
def say_hi():
    print("Hi")

say_hi()


class Transport:
    def __init__(self, model, color, year):
        self.model = model 
        self.color = color 
        self.year = year 
        

class FuelCar(Transport):
    def __init__(self, model, color, year, fuel_tank):
        Transport.__init__(self, model, color, year)
        self.fuel_tank = fuel_tank

    def drive(self):
        print(f"Машина {self.model} едет на топливе")

    def info(self):
        print(f"model - {self.model} \ncolor - {self.color} \nyear - {self.year}\n")

mers_1 = FuelCar("mers - cls", "BLACK", 2016, 100)
mers_1.drive()
mers_1.info()

class ElectroCar(Transport):
    def __init__(self, model, color, year, battery):
        Transport.__init__(self, model, color, year)
        self.battery = battery

    def drive(self):
        print(f"Машина {self.model} едет на электричестве")

    def info(self):
        print(f"model - {self.model} \ncolor - {self.color} \nyear - {self.year}\n")

tesla = ElectroCar("tesla - model x", "Белый", 2022, 100000)
tesla.drive()
tesla.info()


class GybrydCar(FuelCar, ElectroCar):
    pass

    def info(self):
        print(f"model - {self.model} \ncolor - {self.color} \nyear - {self.year}\nfuel_tank - {self.fuel_tank}\n")

    def drive(self, city):
        print(f"Машина {self.model} едет на электричестве и на топливе")
        print(f"Машина {self.model} едет в {city}")

toyota = GybrydCar("toyota - prius", "Белый", 2020, 50)
toyota.drive("Бишкек")
toyota.info()



