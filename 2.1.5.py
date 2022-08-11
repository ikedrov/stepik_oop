'''Создайте класс Constructor, в котором реализованы

метод add_atribute , принимающий на вход название атрибута в виде строки и его значение. При помощи функции setattr необходимо создать или изменить атрибут для ЭК, у которого этот метод был вызван
метод display ,  печатающий на экран словарь __dict__ у ЭК'''

class Constructor:
    def add_atribute(self, x, y):
        setattr(self, x, y)

    def display(self):
        print(self.__dict__)

