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
)""")

class Bank:
    def init(self):
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

        cursor.execute("INSERT INTO klients (full_name, age, adres, email, password) VALUES (?, ?, ?, ?, ?)",
                       (full_name, age, adres, email, password))
        connect.commit()
        
    def set_initial_balance(self, full_name, balance):
        cursor.execute("UPDATE klients SET balance = ? WHERE full_name = ?", (balance, full_name))
        connect.commit()
        
    def top_up_the_account(self, full_name, money):
        cursor.execute("UPDATE klients SET balance = balance + ? WHERE full_name = ?", (money, full_name))  
        connect.commit()
        cursor.execute("SELECT balance FROM klients WHERE full_name = ?", (full_name,))
        balance = cursor.fetchone()
        print(f"Ваш баланс: {balance[0]}")
        
    def take_away_the_money(self, full_name, money):
        cursor.execute("UPDATE klients SET balance = balance - ? WHERE full_name = ?", (money, full_name))  
        connect.commit()
        cursor.execute("SELECT balance FROM klients WHERE full_name = ?", (full_name,))
        balance = cursor.fetchone()
        print(f"Ваш баланс: {balance[0]}")
        if balance[0] < money:
            print(f"Недостаточно средств:\nВаш баланс:{balance[0]}")
        
    def view_the_invoice(self, full_name):
        cursor.execute("SELECT balance FROM klients WHERE full_name = ?", (full_name,))
        balance = cursor.fetchone()
        print(f"Ваш баланс: {balance[0]}")
        
    def main(self):
        print("Добро пожаловать в наш банк!")
        while True:
            print("Выберите действие: ")
            print("0 - Выйти, 1 - Регистрация, 2 - Войти в аккаунт")    
            command = int(input("Введите цифру: "))
            if command == 0:
                break
            elif command == 1:
                full_name = input("Введите полное имя:\n")
                age = input("Введите возраст:\n")
                adres = input("Введите адрес:\n")
                email = input("Введите email:\n")
                password = input("Введите пароль:\n")
                self.register(full_name, age, adres, email, password)
                balance = float(input("Введите начальный баланс:\n"))
                self.set_initial_balance(full_name, balance)
                print("Вы успешно зарегистрированы!")
                print(f"Ваш текущий баланс: {balance}")
            elif command == 2:
                while True:
                    name = input("Введите ваше полное имя:\n")
                    password1 = input("Введите пароль:\n")
                    cursor.execute("SELECT full_name, password FROM klients WHERE full_name = ? AND password = ?", (name, password1))
                    result = cursor.fetchone()
                    if result:
                        print(f"Добро пожаловать, {name}!")
                        while True:
                            command1 = int(input("Выберите действие: 1 - Положить деньги, 2 - Снять деньги, 3 - Посмотреть баланс, 4 - Выйти из аккаунта"))
                            if command1 == 1:
                                money = float(input("Введите сумму для пополнения: "))
                                money = float(input("Введите сумму для пополнения: "))
                                self.top_up_the_account(name, money)
                            elif command1 == 2:
                                money = float(input("Введите сумму для снятия: "))
                                self.take_away_the_money(name, money)
                            elif command1 == 3:
                                self.view_the_invoice(name)
                            elif command1 == 4:
                                print("Вы успешно вышли из аккаунта!")
                                break
                    else:
                        react = input("Неправильное полное имя или пароль. Попробовать снова? (да/нет): ")
                        if react.lower() != "да":
                            break


my_bank = Bank()
my_bank.main()