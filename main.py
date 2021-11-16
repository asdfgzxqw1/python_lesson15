class Person:
    def __init__(self, name, last_name, id, age):
        self.name = name
        self.last_name = last_name
        self.__id_number = id
        self._age = age

    def get_age(self):
        print(self._age)

    def get_id_number(self):
        print(self.__id_number)

    def get_full_name(self):
        print(self.name, self.last_name)

    def set_name(self, name):
        print(self.name)


class Director(Person):
    def __init__(self, name, last_name, id, age):
        super().__init__(name, last_name, id, age)


class Teacher(Person):
    def __init__(self, name, last_name, id, age):
        super().__init__(name, last_name, id, age)


class Student(Person):
    def __init__(self, name, last_name, id, age):
        super().__init__(name, last_name, id, age)



