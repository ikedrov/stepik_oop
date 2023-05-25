
'''
Создайте класс Employee, который имеет следующие методы:

метод __init__, который устанавливает значения приватных атрибутов __name  и __salary: имя работника и его зарплату
 
приватный геттер метод для атрибута __name
 
приватный геттер метод для атрибута __salary
 
приватный сеттер метод для атрибута __salary: он должен позволять сохранять в атрибут __salary только положительные числа. В остальных случаях не сохраняем переданное значение в сеттер и печатаем на экран сообщение "ErrorValue:<value>".
 
свойство title, у которого есть только геттер из пункта 2.
 
свойство reward, у которого геттером будет метод из пункта 3, а сеттером — метод из пункта 4.
'''

class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    def __set_salary(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__salary = value
        else:
            print(f'ErrorValue:{value}')

    title = property(fget = __get_name)
    reward = property(fget = __get_salary, fset = __set_salary)
