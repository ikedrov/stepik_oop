''' Создайте базовый класс  Person, у которого есть:

конструктор __init__, который должен принимать на вход имя и номер паспорта и записывать их в атрибуты name, passport
метод display, который печатает на экран сообщение «<имя>: <паспорт>»;
Затем создайте подкласс Employee , унаследованный от Person. В нем должен быть реализован:

метод  __init__, который принимает именно в таком порядке четыре значения: имя, паспорт, зарплату и отдел. Их нужно сохранить в атрибуты  name, passport, salary,department. При этом создание атрибутов name, passportнеобходимо делегировать базовому классу Person'''

class Person:

    def __init__(self, name, pasport):
        self.name = name
        self.passport = pasport

    def display(self):
        print(f'{self.name}: {self.passport}')

class Employee(Person):

    def __init__(self, name, passport, salary, department):
        super().__init__(name, passport)
        self.salary = salary
        self.department = department


a = Employee('Raul', 886012, 200000, "QA")

a.display()