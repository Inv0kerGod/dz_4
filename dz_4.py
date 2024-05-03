class GeeksPeople:
    def __init__(self,name,email,phone):
        self.name = name
        self.email= email
        self.phone = phone
    def __str__(self):
        return f"имя:{self.name}\nпочта:{self.email}\nтелефон:{self.phone}"
    

class Admin(GeeksPeople):
    def __init__(self, name, email, phone,admin_id,wcreate_group):
        super().__init__(name, email, phone)
        self.admin_id = admin_id
        self.wcreate_group = wcreate_group
    def create_group(self):
        print(f"вы создали группу: {self.wcreate_group}")
    def __str__(self):
        return super().__str__()+ " " + f"\nваш айди админа:{self.admin_id}"
admin = Admin("улан","@ggggggggggggggmail",11111111,23,"17-B\n")
print(admin)
admin.create_group()

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone,teacher_id,group_where_teach):
        GeeksPeople.__init__(self,name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach
    def teach(self):
        print(f"вы преподаете группе: {self.group_where_teach}")
    def __str__(self):
        return super().__str__()+ " " + f"\nваш teacher айди:{self.teacher_id}"
teacher = Teacher("сыймык","@ggggmail",996708381382,18,"17-B\n")
print(teacher)
teacher.teach()

class Student(GeeksPeople):
    def __init__(self, name, email, phone,student_id,group_where_study):
        GeeksPeople.__init__(self,name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study
    def study(self):
        print(f"вы учитесь в группе: {self.group_where_study}")
    def __str__(self):
        return super().__str__()+ " " + f"\nваш студент айди:{self.student_id}"
student = Student("нурдан","@gmail",89148381782,20,"17-B\n")
print(student)
student.study()


class Mentor(Teacher, Student):
    def __init__(self, name, email, phone,  student_id, group_where_teach, teacher_id, group_where_study):
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)
        Student.__init__(self, name, email, phone, student_id, group_where_study)
    def teach(self):
        print(f"ваша группа: {self.group_where_teach}")
    def study(self):
        print(f"вы закончили обучение и преподаете младшей группе {self.group_where_study}")

mentor = Mentor("кудбухон","@gAmail",999999999,"отсутствует","10-B",15,'10-B')
print(mentor)
mentor.study() 
mentor.teach()  
     