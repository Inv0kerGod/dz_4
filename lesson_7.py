import sqlite3 


connect = sqlite3.connect("Geeks.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
                id INT PRIMARY KEY,
                full_name VARCHAR (20) NOT NULL,
                hobby TEXT DEFAULT NULL,
                phone_number INTEGER NOT NULL DEFAULT 996,
                birth_date DATE,
                mark DOUBLE (7, 2) DEFAULT 0.0,
                agreement BOOLEAN DEFAULT FALSE
   )            
   
""")

class Geeks:
    def __init__(self):
        self.full_name = None
        self.hobby = None
        self.phone_number = 0
        self.birth_date = None
        self.mark = 0.0
        self.agreement = None
    def register(self,full_name,hobby,phone_number,birth_date):
        self.full_name = full_name
        self.hobby = hobby
        self.phone_number = phone_number
        self.birth_date = birth_date
        
        cursor.execute(f"""INSERT INTO students (full_name,hobby,phone_number,birth_date)
                       VALUES ("{full_name}",'{hobby}',{phone_number},'{birth_date}')""")
        # cursor.execute("""INSERT INTO students (full_name,hobby,phone_number,birth_date)
        #                VALUES ("?",'?','?',"?")""",full_name,hobby,phone_number,birth_date)
        connect.commit()
        
geeks_students = Geeks()
geeks_students.register("nurdan",'basket',996708381382,"12-02-2004")

        
        






























'''
git clone "ссылку"
git clone -b master ССЫЛКУ
'''
'''git add 
git comit 
git push'''
