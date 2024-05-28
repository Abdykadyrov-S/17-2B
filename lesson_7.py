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

def regiater():
    full_name = input("Введите имя: ")
    hobby = input("Введите хобби: ")
    number = int(input("Введите номер: "))
    birth_date = input("Введите др: ")
    perf = float(input("Введите успеваемость: "))
    he_was = bool(input("Введите успеваемость: "))

    # cursor.execute("""INSERT INTO students 
    #                (full_name, hobby, phone_number, birth_date, performance, he_was)
    #                Values ('?', '?', ?, '?', ?, ?)""", full_name, hobby, number, birth_date, perf, he_was)
    
    cursor.execute(f"""INSERT INTO students 
                   (full_name, hobby, phone_number, birth_date, performance, he_was)
                   Values ('{full_name}', '{hobby}', {number}, '{birth_date}', {perf}, {he_was})""")
    
    connect.commit() 

def all_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print(students)

all_students()

# regiater()
