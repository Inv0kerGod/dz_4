import sqlite3


connect = sqlite3.connect("Geeks.db")
cursor = connect.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               full_name VARCHAR (20) NOT NULL,
               hobby TEXT DEFAULT NULL,
               phone_number INTEGER NOT NULL DEFAULT 996,
               birth_date DATE,
               mark DOUBLE (7, 3) DEFAULT 0.0,
               agreement BOOLEAN DEFAULT FALSE,
               x_cards INT DEFAULT 0,
               coins INT DEFAULT 4
)

""")

class Geeks:
    def __init__(self):
        self.full_name = None
        self.hobby = None
        self.phone_number = 0
        self.birth_date = None
        self.mark = 0.0
        self.agreement = False
        self.x_cards = 0
        self.coins = 4

    def register(self, full_name, hobby, phone_number, birth_date):
        self.full_name = full_name
        self.hobby = hobby
        self.phone_number = phone_number
        self.birth_date = birth_date

        cursor.execute(f"SELECT phone_number FROM students WHERE phone_number = {phone_number}")
        student = cursor.fetchone()
        if student:
            print("Вы уже проходили регистрацию")
        else:
            cursor.execute(f"""INSERT INTO students (full_name, hobby, phone_number, birth_date)
                        VALUES ('{full_name}', '{hobby}', {phone_number}, '{birth_date}')""")
        # cursor.execute("""INSERT INTO students (full_name, hobby, phone_number, birth_date)
        #                VALUES ('?', '?', ?, '?')""", full_name, hobby, phone_number, birth_date)
        
        connect.commit()

    def all_students(self):
        cursor.execute(f"SELECT * FROM students")
        students = cursor.fetchall()
        print(students)

    def add_x_cards(self, amount, id):
        cursor.execute(f"UPDATE students SET x_cards = x_cards + {amount} WHERE id = {id}")
        connect.commit()
        cursor.execute(f"SELECT x_cards FROM students WHERE id = {id}")
        x_cards = cursor.fetchone()
        print("У вас накопилось :", x_cards)
        self.x_cards += amount

    def minus_coin(self, amount, id):
        cursor.execute(f"UPDATE students SET coins = coins - {amount} WHERE id = {id}")
        connect.commit()
        cursor.execute(f"SELECT coins FROM students WHERE id = {id}")
        coins = cursor.fetchone()
        print("У вас осталось :", coins)
        self.coins -= amount

    def delete_student(self, id):
        cursor.execute(f"DELETE FROM students WHERE id = {id}")
        connect.commit()
        print("Студент удален из БД")

    def main(self):
        while True:
            print("Выберите действие: ")
            print("0-выйти, 1-Регистрация, 2-Посмотреть всех пользователей, 3-Добавить Х-карту, 4-удалить студента")
            command = int(input("Введите цифру: "))
            if command == 0:
                break
            elif command == 1:
                name = input("Введите полное имя:\n")
                hobby = input("Введите свое хобби:\n")
                number = int(input("Введите номер телефона:\n"))
                birth_date = input("Введите дату рождения:\n")
                self.register(name, hobby, number, birth_date)

            elif command == 2:
                self.all_students()

            elif command == 3:
                amount = int(input("Введите кол-во Х-карт:\n"))
                id = int(input("Введите id студента:\n"))
                self.add_x_cards(amount, id)

            elif command == 4:
                id = int(input("Введите id студента:\n"))
                self.delete_student(id)

            elif command == 5:
                amount = int(input("Введите кол-во коинов:\n"))
                id = int(input("Введите id студента:\n"))
                self.minus_coin(amount, id)
    

geeks_students = Geeks()
geeks_students.main()



























'''
git clone "ссылку"
git clone -b master ССЫЛКУ
'''
'''git add 
git comit 
git push'''






