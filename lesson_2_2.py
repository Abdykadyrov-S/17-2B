

class Transport:  # Абстрактный класс и Родительский класс
    def __init__(self, model, color):
        self.model = model 
        self.color = color 

#     def movement(self):
#         print("Передвижение")

#     def info(self):
#         print(f"model - {self.model}, color - {self.color}")

# class Airplane(Transport):
#     pass

# air = Airplane("Boing - 747", "White")
# air.info()

class Car(Transport):  # Родительский класс и Дочерний класс 
    def __init__(self, model, color):
        Transport.__init__(self, model, color)
        self.is_start = False

#     def info(self):
#         print(f"model - {self.model}, \ncolor - {self.color}\n")

# mers = Car("mersedes - benz", "White")
# bmw = Car("bnw - m5", "Black")

# class Mersedes(Car): # Дочерний класс 
#     def __init__(self, model, color, is_jump):
#         # super().__init__(model, color)
#         Car.__init__(self, model, color)
#         self.is_jump = is_jump

#     def info(self):
#         print(f"model - {self.model} \ncolor - {self.color} \nis_jump - {self.is_jump}\n")

#     def isjump(self):
#         if self.is_jump == True:
#             print(f"У машины {self.model} есть свойство <<< прыжки >>> ")
#         else: 
#             print(f"У машины {self.model} отсутствует свойство <<< прыжки >>> ")


# "Полиморфизм - это когда один метод выполняет разные действия (должны находится в разных классах)"
# class Animal:
#     def make_sound(self):
#         print("Hello!")

# class Dogs(Animal): 
#     def make_sound(self):
#         print("Gaf - Gaf")

# class Cats(Animal):
#     def make_sound(self):
#         print("Meow - Meow")

# class Cow(Animal):
#     def make_sound(self):
#         print("Moo - Moo")

# animal = Animal()
# dog = Dogs()
# cat = Cats()
# cow = Cow()

# animal.make_sound()
# dog.make_sound()
# cat.make_sound()
# cow.make_sound()

"Инкапсуляция - защита данных"

class Laptops:
    def __init__(self, monitor, keyboard, color):
        self.monitor = monitor # Публичный
        self._keyboard = keyboard # Защишенный 
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
