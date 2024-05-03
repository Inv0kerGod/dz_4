class Fruits:
    weight = "тысяча"
    def __init__(self,frutks,color):
        self.frutks = frutks
        self.color = color
    def info(self):
        print(f'данные: {self.frutks} {self.color} {self.weight}')
frukt = Fruits("банан","yellow")
frukt.info()
#2
class Heroes:
    def __init__(self, name, health, role, rasa):  
        self.name = name.strip('- ,')  
        self.health = int(health.strip('- ,'))  
        self.role = role.strip('- ,') 
        self.rasa = rasa.strip('- ,')  

    def info(self):
        print(f'имя {self.name}, хп {self.health}, роль {self.role}, раса {self.rasa}')
        
    def attack(self):
        if self.health == 100 or self.health == 50: 
            print(f"{self.name} атакует огненным шаром")
    
    def damage(self, damage_amount):
        if self.health == 100 or self.health == 50:  
            self.health - damage_amount 
            print(f"{self.name} потеряла {damage_amount} хп")

info1 = Heroes("Нурдан", "100", "колдун", "человек")
info2 = Heroes("сестра Нурдана", "50", "змея", "ящеры")
info3 = Heroes("младшая сестра нурдана", "70", "зомби", "человек")

info1.info()
info2.info()
info3.info()

info1.attack()
info2.damage(20)



#экземпляр = это обьекты созданные по шаблону класса


