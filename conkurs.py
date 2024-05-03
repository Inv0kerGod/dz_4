class Person:
    def __init__(self,fullname,age,password):
        self.fullname = fullname
        self.age = age
        self.__password = password
    
    def set_password(self):
       self.__password= input("введите пароль: ")
    @property
    def passwrod(self):
        return self.__password
    def info(self):
        print(f"ваше полно имя:{self.fullname} \nи ваш возраст {self.age}")
    def get_password(self):
        print(f"ваш пароль: {self.passwrod}")

person = Person("Роман",20,0)
person.info()
person.set_password()
person.get_password()

# class Teacher(Person):
#     def __init__(self, fullname, age,subject):
#         super().__init__(fullname, age)
#         self.subject = subject
#     def show_infp(self):
#         print(f"ваше полно имя:{self.fullname} \nи ваш возраст {self.age} \nи род деятельности {self.subject}")
# teacher = Teacher("Рехан",20,"математика")
# teacher.info()
# class Student(Person):
#     def __init__(self, fullname, age,student_id):
#         super().__init__(fullname, age)
#         self.student_id = student_id
#     def show_info(self):
#         print(f"ваше полно имя:{self.fullname}\nи ваш возраст {self.age}\nи айди {self.student_id}")
# student = Student("Кома",20, 123123)
# student.info()






