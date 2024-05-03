#1
class Computer:
    def __init__(self,cpu,memory):
        self.__memory = memory
        self.__cpu = cpu
    @property
    def memory(self):
        return self.__memory
    @property
    def cpu(self):
        return self.__cpu

    def __make_computations(self):
        print(f"результат арифметических операций:\nсложение {self.__memory + self.__cpu}\nвычитание: {self.__cpu - self.__memory}\nумножение:  {self.__cpu * self.__memory}\nделение: {self.__cpu / self.__memory} ")
    @property
    def make_computations(self):
        return self.__make_computations
    
computer = Computer(10,512)
computer.make_computations()
class Laptop(Computer):
    def __init__(self, cpu, memory,memory_card):
        self.__memory = memory
        self.__cpu = cpu
        self.__memory_card = memory_card
    @property
    def memory_card(self):
        return self.__memory_card
    def info(self):
        print(self.__cpu,self.__memory,self.__memory_card)
laptop = Laptop(15,512,30)
print(laptop.memory_card)
laptop.info()
    