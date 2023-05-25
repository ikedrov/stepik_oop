'''
Создайте класс TemperatureConverter, который имеет следующие методы:

 статический метод celsius_to_fahrenheit, который принимает температуру в градусах Цельсия и переводит ее в градусы по Фаренгейту
 статический метод fahrenheit_to_celsius, который принимает температуру в градусах по Фаренгейту и переводит ее в градусы по Цельсия
'''

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * (9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * (5 / 9)
