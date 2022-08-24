'''
Создайте класс Rectangle, у которого есть:

конструктор __init__, принимающий 2 аргумента: длину и ширину.
свойство area, которое возвращает площадь прямоугольника;
'''

class Rectangle:

    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b
        self.__area = None

    @property
    def sides(self):
        return self.side_a, self.side_b

    @sides.setter
    def sides(self, v1, v2):
        self.side_a = v1
        self.side_b = v2
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.side_a * self.side_b
        return self.__area

r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print(r1.area)
print(r2.area)

