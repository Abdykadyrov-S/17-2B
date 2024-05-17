"ООП строится вокруг четырёх основных принципов: абстракция, инкапсуляция, наследование и полиморфизм. "

"Абстракция или же Абстрактный класс - он собирает в себе все обобщенные атрибуты и методы объекта"
"Наследование - это когда один класс(дочерний) наследует все о другого класса(родительский) . Дочерние классы наследуют атрибуты родительских, а также могут переопределять атрибуты и добавлять свои."
class Transport:  # Абстрактный класс и Родительский класс
    def __init__(self, model, color):
        self.model = model 
        self.color = color 

    def movement(self):
        print("Передвижение")

    def info(self):
        print(f"model - {self.model}, color - {self.color}")

    def __str__(self):
        return f"model - {self.model}, color - {self.color}"


class Car(Transport):  # Родительский класс и Дочерний класс 
    def __init__(self, model, color):
        Transport.__init__(self, model, color)
        self.is_start = False

    def info(self):
        print(f"model - {self.model}, color - {self.color}, is_start - {self.is_start}")

    def __str__(self):
        return super().__str__() + ", " +  f"is_start - {self.is_start}"

mers = Car("mersedes - benz", "White")
bmw = Car("bnw - m5", "Black")
# bmw.info()
print(bmw)

class Mersedes(Car): # Дочерний класс 
    def __init__(self, model, color, is_jump):
        # super().__init__(model, color)
        Car.__init__(self, model, color)
        self.is_jump = is_jump

    def info(self):
        print(f"model - {self.model}, color - {self.color}, is_start - {self.is_start}, is_jump - {self.is_jump}\n")

    def __str__(self):
        return super().__str__() + ", " +  f"is_jump - {self.is_jump}"

    def isjump(self):
        if self.is_jump == True:
            print(f"У машины {self.model} есть свойство <<< прыжки >>> ")
        else:
            print(f"У машины {self.model} отсутствует свойство <<< прыжки >>> ")


mers_1 = Mersedes("mers - cls", "BLACK", True)
mers_2 = Mersedes("mers - e63s", "GREY", False)
print(mers_1)
# mers_1.info()
# mers_2.info()
mers_1.isjump()
mers_2.isjump()
mers_1.movement()

"Полиморфизм - это когда один метод выполняет разные действия (должны находится в разных классах)"
# class Animal:
#     def make_sound(self):
#         pass 

# class Dogs(Animal): 
#     def make_sound(self):
#         print("Gaf - Gaf")

# class Cats(Animal):
#     def make_sound(self):
#         print("Meow - Meow")

# class Cow(Animal):
#     def make_sound(self):
#         print("Moo - Moo")

# dog = Dogs()
# cat = Cats()
# cow = Cow()

# dog.make_sound()
# cat.make_sound()
# cow.make_sound()


# def make_sound():
#     print("GAF-GAF")

# def make_sound():
#     print("MEOW")

# def make_sound():
#     print("MOO")


# make_sound()
# make_sound()
# make_sound()
# make_sound()


# number = 5
# number = 7

# print(number)