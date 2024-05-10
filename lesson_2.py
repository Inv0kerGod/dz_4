"принципы ооп"
"наследование и абстракция"

# class People:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

class Parents():
    def __init__(self,name,age,):
        self.name = name
        self.age = age
    def info(self):
        print(f"{self.name} ,{self.age}")
    def swim(self):
        print("я не умею плавать")
        
dade = Parents("Роман",30)
# print(dade.name) 
# dade.info()
# dade.swim()
class Man:
    def __init__(self,glaza,rost):
        self.glaza = glaza
        self.rost = rost
    def info(self):
        print(f"{self.glaza} ,{self.rost}")
        
man = Man("синие",180)
man.info()
  
class Children(Parents,Man):
    def __init__(self,name,age,glaza,rost):
        super().__init__(name,age)
        super().__init__(glaza,rost)
        # self.property = property
    def swim(self):
        print("я умею плавать")

child = Children("nurdan",20,"синие",190)
child.info()
child.swim()



class Animals:
    def __init__(self,name,eyes):
        self.name = name
        self.eyes = eyes
        
class Dogs(Animals):
     def make_sound(self):
        print("гав гав")

class Kats(Animals):
     def make_sound(self):
        print("мяу мяу")
        
class Fish(Animals):
    def make_sound(self):
        print("блуп блуп")
        
dog = Dogs("Роман","карие")
cat = Kats("ROMAN","zelenyu")
fish = Fish("nemo","yellow")
dog.make_sound()
cat.make_sound()
fish.make_sound()
        