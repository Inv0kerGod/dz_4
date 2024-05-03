class MagicCalculator:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __str__(self):
        return f"\nрезультат арифметических действий:{self.number_1}\nрезультат арифметических действий:{self.number_2}"

    def __add__(self, other):
        new_number_1 = self.number_1 + other.number_1
        new_number_2 = self.number_2 + other.number_2
        return MagicCalculator(new_number_1, new_number_2)

    def __sub__(self, other):
        new_number_1 = self.number_1 - other.number_1
        new_number_2 = self.number_2 - other.number_2
        return MagicCalculator(new_number_1, new_number_2)

    def __mul__(self, other):
        new_number_1 = self.number_1 * other.number_1
        new_number_2 = self.number_2 * other.number_2
        return MagicCalculator(new_number_1, new_number_2)

    def __truediv__(self, other):
        new_number_1 = self.number_1 / other.number_1
        new_number_2 = self.number_2 / other.number_2
        return MagicCalculator(new_number_1, new_number_2)

calculator = MagicCalculator(50, 10)
calculator1 = MagicCalculator(10, 2)
print(calculator + calculator1, calculator - calculator1, calculator * calculator1, calculator / calculator1)


class Book:
    def __init__(self,Title, author, year_publication):
       self.Title = Title
       self.Author = author
       self.Year_publication = year_publication
    def __str__(self):
        return f"название книги:{self.Title}\nимя автора:{self.Author}\nгод выпуска:{self.Year_publication}\n"
    def __gt__(self,other): # > ключ для вызова
        return self.Year_publication > other.Year_publication
    def __lt__(self,other): # < ключ для вызова
        return self.Year_publication < other.Year_publication
    def __eq__(self,other): # == ключ для вызова
        return self.Year_publication == other.Year_publication
    def __ne__(self,other): # != ключ для вызова
        return self.Year_publication != other.Year_publication
    def __ge__(self,other): # != ключ для вызова
        return self.Year_publication >= other.Year_publication
    def __le__(self,other): # != ключ для вызова
        return self.Year_publication <= other.Year_publication

book = Book("Война и мир","Л.Н.Толстой",1873)
book1 = Book("Го́рдость и предубежде́ние"," Джейн Остин",1813)
print(book)
print(book1)
print(book>book1,book<book1,book==book1,book!=book1,book>=book1,book<=book1)
        


    