def cloce():
    import random
    import sqlite3
    connect = sqlite3.connect("Player.db")
    cursor = connect.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
                    id INT PRIMARY KEY,
                    user_name VARCHAR (20) NOT NULL,
                    phone_number INTEGER NOT NULL DEFAULT 996,
                    birth_date DATE
                    
        
    )
""")
    class Player:
        def __init__(self):
            self.user_name = None
            self.phone_number = 0
            self.birth_date = None
        def register(self):
            self.user_name = input("Введите имя пользователя: ")
            self.phone_nubmer = input("Введите номер телефона: ")
            self.birth_date = input("Введите дату рождения: ")
            
            cursor.execute("""INSERT INTO players (user_name,phone_number,birth_date)
                        VALUES (?,?,?)""",(self.user_name, self.phone_number,self.birth_date))
            connect.commit()
            
    player_1 = Player()
    player_1.register()

    while True:
        choice = input("Выберите, во что играть: 1 - Герои и Монстры, 2 - Камень Ножницы бумага, 3-Генератор паролей\n")
        if choice == "1":
                Monstr = 1000
                Hero = 200
                fire = 300
                molnya = 500
                attack_monstr = 50
                attack_monstr1 = 100
                attack_monstra = 40
                attack_monstra1 = 80
                hill = 5
                hill1 = 20
                w = 'MONSTR'
                avtor1 = input("Приветствую, добрый путник! Меня зовут Автор, а тебя как зовут?\n")
                avtor = input(f"Очень приятно познакомиться, {avtor1.upper()}.\n>>> Дальше >>>\n")
                avtor = input(f"Что это, {avtor1.upper()}? Вон в той стороне {w}! О нет, прошу останови его.\nПринять задание = 1\nОтказаться = 2\n") 
                if avtor == "2":
                        e = input("Вас заклеймили трусом и закидали камнями. Вы с позором покинули королевство Фиор.\nВернуться в главное меню = 1\n")
                        while e != "1":
                            if e == "1":
                                continue
                            elif e != "1":
                                 e = input("Вернутсья в меню = 1\n")
                elif avtor == "1":
                        avtor = input(f"\n{avtor1.upper()}, ваш противник {w}\nХарактеристики: здоровье {Monstr}\nОсобые умения {w}A:\n>>> удар когтем\n>>> удар хвостом\n>>> дальше >>>\n>>> дальше >>>\n>>> дальше >>>")
                        hero = input(f"\nИтак {avtor1.upper()}, Вот твоя характеристика здоровье:{Hero}\n Особые умения:↓↓↓\n1 - Огненный шар (наносит 300 урона)\n2 - Удар молнией (наносит 500 урона)\n3 - Сбросить ядерную бомбу\n")
                        input(f"да начнется битва!!!\n")
                        while Hero > 0 and Monstr > 0: 
                                attack_choice = input(f"\nВаше здоровье: {Hero}\nВыберите атаку:\n1 - Огненный шар (наносит 300 урона)\n2 - Удар молнией (наносит 500 урона)\n3 - Сбросить ядерную бомбу\n>>>Продолжить\n")
                                if attack_choice == "1":
                                    asmr = input(f"\nВы атакуете {w}A огненным шаром. Нажмите, чтобы продолжить >>>")
                                    Monstr -= fire
                                    input(f"\nВы атаковали {w}A огненным шаром и нанесли {fire} урона. У {w}A осталось {Monstr} здоровья.\n>>>Нажмите\n")
                                elif attack_choice == "2":
                                    Monstr -= molnya
                                    input(f"Вы атаковали {w}A ударом молнии и нанесли {molnya} урона. У {w}A осталось {Monstr} здоровья.\n")
                                elif attack_choice == "3":
                                    Monstr = 0
                                    print(f"Вы сбросили ядерную бомбу! {w} не пережил эту атаку!!!\nвпрочем как и все включая вас...\n")
                                    input("Нажмите чтобы продолжить:\n")                   
                                if Monstr > 0:
                                    input(f"{w} ужасно разозлился\n>>>Нажмите\n\n")
                                    dam_monst = ['1','2']
                                    dam = random.choice(dam_monst)
                                    if dam == '1':
                                        monster_damage = random.randint(attack_monstr,attack_monstr1)
                                        Hero -= monster_damage
                                        print(f"{w} атаковал Когтем и нанес {monster_damage} урона.")
                                    elif dam == '2':
                                        monster_damage2 = random.randint(attack_monstra,attack_monstra1)
                                        Hero -= monster_damage2
                                        print(f"{w} атаковал Хвостом и нанес {monster_damage2} урона.")
                                    if Hero > 0:
                                        print(f"У вас осталось {Hero} здоровья.\nвы истекаете кровью вам срочно нужно побыстрее одолеть {w}A!!!\n")
                                    
                                if Hero > 0 and Monstr >=0 and Monstr !=0:
                                        s =  input(f"Выберите действие:\nбежать как трус - 1\nТолкнуть речь с героическим лицом - 2\n")
                                        if s == "1":
                                            print("Вас заклеймили трусом и закидали камнями вы с позором покинули королевство Фиор\n")
                                            break
                                        elif s == "2":
                                            q = input(f"\nА может все же дать по газам?\nДать по газам - 1\nВсе же толкнуть речь - 2\n")
                                            if q == "1":
                                                print("Вас заклеймили трусом и закидали камнями вы с позором покинули королевство Фиор\n")
                                                break
                                            elif q == "2":
                                                ccc = ['1','2','3']
                                                qwe = random.choice(ccc)
                                                if qwe == '1':
                                                    input(f"Вы все же решаетесь толкнуть речь:\n<<Победитель это неудачник который не сдался!!!(наверное)\n>>>Нажмите чтобы продолжить\n")
                                                elif qwe == '2':    
                                                    input(f"Вы все же решаетесь толкнуть речь:\n<<Не важно как ты бьешь важно то какой держишь удар!!!(наверное)\n>>>Нажмите чтобы продолжить\n")
                                                elif qwe == '3':   
                                                    input(f"Вы все же решаетесь толкнуть речь:\n<<Доброе всегда побеждает зло!!!(наверное)\n>>>Нажмите чтобы продолжить\n")
                                            hillka = random.randint(hill, hill1)
                                            Hero+=hillka
                                            input(f"Речь повысила ваш боевой дух и вы восстановили себе {hillka} единиц здоровья\nУ вас теперь {Hero}\n>>>Ок\n")
                                                

                                if Hero <= 0:
                                    print("Вы пали в бою... Игра окончена.\n")
                                    continue
            
                        if attack_choice == "3":
                            input("Поздравляем Вы всех убили!\n Вы победили монстра и спасли королевство Фиор!\nНу как спасли...\n>>>Далее\n")
                            l = input(f"Создатель сего произведения: Турдукулов Н.M\nВсем спасибо за внимание\nВернуться в главное меню = 2\n")
                            while l != "2":
                                if l == "2":
                                    continue
                                elif l != "2":
                                    l = input("Вернутсья в меню = 2\n")
                            continue
                        if Monstr <= 0:
                                input("Поздравляем! Вы победили монстра и спасли королевство Фиор!\n>>>Далее\n")
                        l = input(f"Создатель сего произведения: Турдукулов Н.M\nВсем спасибо за внимание\nВернуться в главное меню = 2\n")
                        while l != "2":
                            if l == "2":
                                continue
                            elif l != "2":
                                l = input("Вернутсья в меню = 2\n")                       
                            continue
        elif choice =="2":
            while True:
                action = input("Выберите действие: 1-начать, 2-выйти\n")
                if action == "2":
                    break
                while True:
                    player_choice = input("Камень, Ножницы, Бумага: ")
                    possible_actions = ["Камень", "Ножницы", "Бумага"]
                    computer_choice = random.choice(possible_actions)
                    print(f"Вы выбрали {player_choice}, компьютер выбрал {computer_choice}.")
                    
                    if player_choice == computer_choice:
                        print("Ничья!")
                    elif (player_choice == "Камень" and computer_choice == "Ножницы") or \
                        (player_choice == "Ножницы" and computer_choice == "Бумага") or \
                        (player_choice == "Бумага" and computer_choice == "Камень"):
                        print("Вы выиграли!")
                    else:
                        print("Вы проиграли.")
                    
                    repeat = input("Выберите действие: 1-еще раз, 2-вернуться в меню\n")
                    if repeat == "2":
                        break
        elif choice == "3":
            password = print("Добро пожаловать в генератор паролей:")
            while True:
                password = input("Введите любые Символы, Числа, и Буквы:\n")
                random_password = 30
                random_password1 = "".join(random.choice(password)for i in range(random_password))
                print(f"\nВаш случайный пароль:\n{random_password1}\n")
                m = input("Выберите действие:\nСгенерировать еще один пароль = 1\nВернуться в меню = 2\n")
                if m == "1":
                    continue
                elif m == "2":
                    break
if __name__ == "__main__":
    cloce()






































"""попробуй сделать игру которая обьединяла бы несколько мини игр например каменьножницы бумагу
    или же угадай число или же игру про какого то персонажа чтобы у него были какие то виды атак 
    например огненый шар луч смерти. адава кедавра и тд и чтобы у каждой способности был свой урон
    можно так же добавить чтобы при использовании умения в терминал выводилось будто бы персонаж издовал звуки или же
    произносил заклинание и другие слова так же добавить монстра с которым он сражался бы
    чтобы у того было определенное кол во хп которое отмималось бы когда герой использовал бы свою атаку
    можно добавить регистрацию в самом начале меню и по типу имя возраст и тд и записывать все это в бд либо же если окажется слишком сложно 
    сделать лишь последнюю игру но с более продуманой логикой урона маны и добавить еще парочку монстров
    """