" ООП - Объектно Ориентрованное Программирование "
" DRY - Don`t Repeat Yourself == не повторяй себя"

"ABC - верхний регистр"

"abc - нижний регистр"

super_electro_car_2 = 1 # змеиный регистр

SuperElectroCar2 = 2 # верблюжий регистр

class SuperCar: # чертеж или же шаблон 
    wheels = 4 # Атрибут/поле/свойства класса
    "__init__ - конструктор"
    " self - ссылка на текущий объект "
    def __init__(self, model, color):
        self.model = model # Атрибут/поле/свойства объекта 
        self.color = color 
        self.is_start = False 

    def info(self):
        print(self.model, self.color)

    def start(self):
        self.is_start = True
        print(f"Машина {self.model} заведена")

    def drive(self, city):
        if self.is_start == True:
            print(f"Mашина {self.model} едет в {city}")
        else:
            print("Заведи машину что бы поехать")

    def stop(self):
        self.is_start = False
        print(f"Машина {self.model} заглушена")

mers = SuperCar("mersedes - benz", "White")
bmw = SuperCar("bnw - m5", "Black")
# print(mers.model, mers.color)
# print(bmw.model, bmw.color)
mers.info()
bmw.info()

mers.start()
bmw.start()
mers.stop()
bmw.stop()
mers.drive("г.ОШ")
bmw.drive("г.Бишкек")

