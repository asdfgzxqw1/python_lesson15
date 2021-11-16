from main import Person,Teacher,Director,Student

director = Director('Тобирама ', 'Сенджу', 69)
director2 = Director('Какаши', 'Хатаке', 77)

teacher1 = Teacher('Ирука ', 'Умино', 37)
teacher2 = Teacher('Шикамару', 'Нара', 39)

student1 = Student('Обита', 'Учиха', 16)
student2 = Student('Gabe' 'Newell' , 17)

seq = [director, director2, teacher1, teacher2, student1, student2]
for i in seq:
    print(seq)
