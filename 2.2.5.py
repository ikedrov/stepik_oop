'''Создайте класс Person, у которого есть:

конструктор __init__, принимающий имя, фамилию и возраст. Их необходимо сохранить в атрибуты экземпляра first_name , last_name, age.
метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае;'''

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.last_name + ' ' + self.first_name

    def is_adult(self):
        return self.age >= 18

p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())
print(p1.is_adult())