

class Car:
    wheels = 4 # Атрибут/поле/свойства класса
    "__init__ - конструктор"
    " self - ссылка на текущий объект "
    def __init__(self, model, color): 
        self.model = model # Атрибут/поле/свойства объекта 
        self.color = color
        self.is_start = False

    def drive(self, city):
        if self.is_start == True:
            print(f"Mашина {self.model} едет в {city}")
        else:
            print("Заведи машину что бы поехать")

    def info(self):
        print(self.model, self.color)

    def start(self):
        self.is_start = True
        print(f"Машина {self.model} заведена")

    def stop(self):
        self.is_start = False
        print(f"Машина {self.model} заглушена")

    

# mers = Car("mersedes - benz", "White")
# bmw = Car("bmw - m5", "Black")

# bmw.info()
# bmw.start()
# bmw.stop()
# bmw.start()
# bmw.drive("Ош")
# mers.info()

# print(mers.model, mers.color)
# print(bmw.model, bmw.color)
# mers.info()
# bmw.info()


class Apple:
    def __init__(self, color):
        self.color = color
        self.weigth = 0

    def year(self):
        self.weigth = 0
        while self.weigth < 5:
            print(f"Вес {self.weigth}")
            self.weigth += 1

    def eat(self):
        print("Яюлоко съели!")

apple = Apple("RED")
apple.eat()
apple.year()

