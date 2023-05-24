'''
Создайте класс Rectangle, который имеет следующие методы:

метод __init__, который устанавливает значения атрибутов width и height
 
метод area, который возвращает площадь прямоугольника
 
метод perimeter , который возвращает периметр прямоугольника
'''

class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)