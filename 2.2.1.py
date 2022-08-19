'''
 Создайте класс Vehicle, у которого есть:

конструктор __init__, принимающий максимальную скорость и пробег. Их необходимо сохранить в атрибуты экземпляра max_speed и mileage соответственно
'''

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)