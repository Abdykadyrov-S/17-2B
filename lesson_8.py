import sqlite3

" БД - База Данных "
" СУБД - Система Управления Базой Данных "

connect = sqlite3.connect("Geeks.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (20) NOT NULL ,
        hobby TEXT DEFAULT NULL ,
        phone_number INT NOT NULL DEFAULT 996 ,
        birth_date DATE ,
        performance DOUBLE (6,5) DEFAULT 0.0 ,
        he_was BOOLEAN DEFAULT FALSE
)""")


class Geeks:
    def __init__(self):
        self.full_name = None
        self.hobby = None
        self.phone_number = None
        self.birth_date = None
        self.performance = 0.0
        self.he_was = False


    def regiater(self):
        full_name = input("Введите имя: ")
        hobby = input("Введите хобби: ")
        number = int(input("Введите номер: "))
        birth_date = input("Введите др: ")
        perf = float(input("Введите успеваемость: "))
        he_was = bool(input("Явка: "))

        # cursor.execute("""INSERT INTO students 
        #                (full_name, hobby, phone_number, birth_date, performance, he_was)
        #                Values ('?', '?', ?, '?', ?, ?)""", full_name, hobby, number, birth_date, perf, he_was)
        
        cursor.execute(f"SELECT phone_number FROM students WHERE phone_number = {number}")
        student = cursor.fetchone()

        if student:
            print("Вы уже прошли регистрацию")
        else:


            cursor.execute(f"""INSERT INTO students 
                        (full_name, hobby, phone_number, birth_date, performance, he_was)
                        Values ('{full_name}', '{hobby}', {number}, '{birth_date}', {perf}, {he_was})""")
        
        connect.commit() 


    def all_students(self):
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        print(students)

    def update_student_hobby(self):
        id = int(input("Введите id студента у которого новый хобби: : "))
        hobby = input("Введите хобби: ")

        cursor.execute(f"UPDATE students SET hobby = '{hobby}' WHERE id = {id}")
        connect.commit()

    def update_student(self):
        id = int(input("Введите id студента: "))
        full_name = input("Введите имя: ")
        hobby = input("Введите хобби: ")
        number = int(input("Введите номер: "))
        birth_date = input("Введите др: ")
        perf = float(input("Введите успеваемость: "))
        he_was = bool(input("Явка: "))

        cursor.execute("""UPDATE students 
                       SET full_name = ?, hobby = ?, phone_number = ?, birth_date = ?, performance = ?, he_was = ? 
                       WHERE id = ?  """, ( full_name , hobby, number, birth_date, perf, he_was, id))
        
        connect.commit()

    def delete_student(self):
        id = int(input("Введите id студента которого хотите удалить: "))
        cursor.execute(f"DELETE FROM students WHERE id = {id}")
        connect.commit()
        print("Студент удален из БД")

    def main(self):
        while True:
            print("Выберите действие: ")
            print("0-Выйти, 1-Регистрация, 2-Все пользователи, \n3-Обновить хобби студента, 4-Удалить")
            command = int(input("Выберите цифру: "))
            if command == 0:
                break
            elif command == 1:
                self.regiater()
            elif command == 2:
                self.all_students()
            elif command == 3:
                self.update_student_hobby()
            elif command == 4:
                self.delete_student()
            elif command == 5:
                self.update_student()

student = Geeks()
student.main()