"инкапсуляция"
# class Laptops:
#     def __init__(self,model,os,memory ):
#         self.model = model #публичный
#         self._os = os #защищенный
#         self.__memory = memory #приватный
        
#     # @ декоратор
#     @property
#     def memory(self):
#         return self.__memory
        
#     def info(self): #ge,kbxysq
#         print(f"model {self.model}, {self._os}")
#         self._desktop()
    
#     def _desktop(self):
#         print("рабочий стол")
        
#     def __password(self):
#         print("passwrod = 1234")
#     @property
#     def password(self):
#         return self.__password
# huawei = Laptops("huawei", "window 11", 512)
# # print(huawei.model)
# # print(huawei._os)
# # print(huawei.memory)
# huawei.info()
# print(huawei.memory)
# # huawei.desktop()
# huawei.password()




# def users(value):
#     def start():
#         print("hello world")
#         value()
#         print("bye")
#     return start


# @users
# def starst():
#     print("hello")
# starst()
   



# множественное наследование


class Father:
    def __init__(self,name,age,beard):
        self.name = name
        self.age = age
        self.beard = beard
    def work(self):
        print("работает")

class Mather:
    def __init__(self,name,age,manikur):
        self.name = name
        self.age = age
        self.manikur = manikur
    def cook(self):
        print("готовка")
class Child(Father,Mather):
    def __init__(self, name, age,beard,manikur,toys):
        Father.__init__(self,name, age,beard)
        Mather.__init__(self,name,age,manikur)
        self.toys = toys
    def cook(self):
        print("не умею готовить")
child = Child('роман',20,"борода",20,"игрушка")

print(child.name,child.age,child.beard,child.manikur,child.toys)
child.cook()
child.work()
        
        
        

