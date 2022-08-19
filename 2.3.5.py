'''Создайте базовый класс Person, у которого есть:

метод __init__, принимающий имя и возраст человека. Их необходимо сохранить в атрибуты экземпляра nameи age соответственно
метод display_person_info , который печатает информацию в следующем виде:
Person: {name}, {age}
Затем создайте класс Company , у которого есть:

метод __init__, принимающий название компании и город ее основания. Их необходимо сохранить в атрибуты экземпляра company_name  и location соответственно
метод display_company_info , который печатает информацию в следующем виде:
Company: {company_name}, {location}
И в конце создайте класс Employee , который:

имеет метод __init__, принимающий имя человека, его возраст, название компании и город основания. Необходимо создать атрибут personal_data и сохранить в него экземпляр класса Person. И также создать атрибут work  и сохранить в него экземпляр класса Company '''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')

class Company:

    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')

class Employee:

    def __init__(self, name, age, company_name, location):
        self.personal_data = Person(name, age)
        self.work = Company(company_name, location)

emp = Employee('Jessica', 28, 'Google', 'Atlanta')
print(emp.personal_data.name)
print(emp.personal_data.age)
emp.personal_data.display_person_info()
print(emp.work.company_name)
print(emp.work.location)
emp.work.display_company_info()