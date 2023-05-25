'''
Перед вами имеется реализация класса Circle. Ваша задача добавить в него следующее:

класс-метод from_diameter, принимающий диаметр круга. Метод from_diameter должен возвращать новый экземпляр класса Circle(учитывайте, что экземпляры круга создаются по радиусу);
 
статик-метод is_positive, принимающий одно число. Метод is_positive должен возвращать ответ является ли переданное число положительным
 
статик-метод area, который принимает радиус и возвращает площадь круга. Для этого воспользуйтесь формулой
p
i
∗
r
2
pi∗r 
2
  и в качестве значения pi возьмите 3.14
'''


class Circle:

    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @classmethod
    def from_diameter(cls, d):
        return cls(d/2)

    @staticmethod
    def is_positive(num):
        return num >= 0

    @staticmethod
    def area(r):
        return 3.14 * r ** 2