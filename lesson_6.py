# from test import add, sub # точечный импорт 

# add(4,5)
# sub(4,5)

# from test import add as abc

# abc(3,5)



# from test import * # Из модуля импортируем все
# mult(2,8)
# add(2,8)

# import test # импорт модуля

# test.add(2,3)
# test.mult(2,3)

# from secret.test import test 

# from secret.test.test import mult, add

# mult(5,5)
# add(5,5)

# from test_2 import add

# add(6,7)




""" Декомпозиция - разделение кода по модулям """



"  Кастомные модули : start.py , lesson_1.py , test "

" Встроенные(вложенные) модули : random , math , time , datetime "


# import random , time

# luck_num = random.randint(1,10)
# print(luck_num)

# while True:
#     time.sleep(2)
#     print("Loading.....")


" Внешние модули "

from termcolor import cprint 

cprint("Hello World!", color="green", on_color="on_red", attrs=["bold"])

