import sqlite3

connect = sqlite3.connect("Bank.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS klients (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               full_name VARCHAR (20) NOT NULL,
               age INTEGER DEFAULT 0,
               adres TEXT DEFAULT NULL,
               email TEXT DEFAULT NULL,
               balance FLOAT DEFAULT 0.0,
               password TEXT DEFAULT NULL
)
""")

class Bank:
    def __init__(self):
        self.full_name = None
        self.age = None
        self.adres = None
        self.email = None
        self.balance = None
        self.password = None
        
    def register(self, full_name, age, adres, email, password):
        self.full_name = full_name
        self.age = age
        self.adres = adres
        self.email = email
        self.password = password
        cursor.execute("""INSERT INTO klients (full_name, age, adres, email, balance, password)
                          VALUES (?, ?, ?, ?, ?, ?)""", (full_name, age, adres, email, 0, password))    
        connect.commit()
        
    def top_up_the_account(self,money):
        cursor.execute(f"UPDATE klients SET balance = balance + {money} WHERE full_name = {'full_name'}")  
        connect.commit()
        cursor.execute(f"SELECT balance FROM klients WHERE full_name = {'full_name'}")
        balance = cursor.fetchone()
        print(f"Ваш баланс: {balance}")
        
    def take_away_the_money(self,money):
        cursor.execute(f"SELECT balance FROM klients WHERE full_name = {'full_name'}")
        balance = cursor.fetchone()
        if balance and balance[0] >= money:
            cursor.execute(f"UPDATE klients SET balance = balance - {money} WHERE full_name = {'full_name'}")  
            connect.commit()
            print(f"Ваш баланс после снятия: {balance[0] - money}")
        else:
            print(f"Недостаточно средств:\nВаш баланс: {balance[0] if balance else 'недоступен'}")
        
    def view_the_invoice(self, full_name):
        cursor.execute(f"SELECT balance from Klients WHERE full_name = {'full_name'}")
        balance = cursor.fetchone()
        print(f"Ваш баланс: {balance[0] if balance else 'недоступен'}")
        
    def main(self):
        while True:
            print("Выберите действие: ")
            print("0-выйти, 1-Регистрация, 2-Банкомат")    
            command = int(input("Введите цифру: "))
            if command == 0:
                break
            elif command == 1:
                full_name = input("Введите полное имя:\n")
                age = int(input("Введите Возраст:\n"))
                adres = input("Введите адрес:\n")
                email = input("Введите email:\n")
                password = input("Введите Пароль:\n")
                self.register(full_name, age, adres, email, password)
            elif command == 2:
                full_name = input("Введите свое полное имя:\n")
                password1 = input("Введите Пароль:\n")
                cursor.execute("SELECT password FROM klients WHERE full_name = ?", (full_name,))
                correct_password = cursor.fetchone()
                if correct_password and correct_password[0] == password1:
                    while True:
                        command1 = int(input("Выберите действие: 1-Положить деньги 2-Снять деньги 3-Посмотреть баланс 4-Выйти\n"))
                        if command1 == 1:
                            money = float(input("Введите насколько пополнить счет: "))
                            self.top_up_the_account(full_name, money)
                        elif command1 == 2:
                            money = float(input("Введите сколько снять со счета: "))
                            self.take_away_the_money(full_name, money)
                        elif command1 == 3:
                            self.view_the_invoice(full_name)
                        elif command1 == 4:
                            break
                else:
                    print("Неправильное полное имя или пароль")

my_bank = Bank()
my_bank.main()
