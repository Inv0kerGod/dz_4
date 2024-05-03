class Person:
    def __init__(self,fullname,age):
        self.fullname = fullname
        self.age = age
    is_married = True
    def introduce_myself(self):
        print(f"ваше полное имя: {self.fullname} и ваш возраст: {self.age}")
student = Person("вячеслав",20)
student.introduce_myself

class Teacher(Person):
    salary = 0
    def __init__(self, fullname, age,experience):
        super().__init__(fullname, age)
        self.experience = experience
    def introduce_myself(self):
        print(f"ваше имя:{self.fullname} ваш возраст:{self.age} вот опыт работы: {self.experience}")
    def sumSalary(self):
        self.salary = self.experience*3000
teacher = Teacher("роман",20,3)
teacher.introduce_myself
teacher.sumSalary(10)
        
    
        
    
        
        