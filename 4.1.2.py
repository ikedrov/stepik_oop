'''Создайте базовый класс Vehicle, у которого есть:

конструктор __init__, принимающий название транспортного средства, его максимальную скорость и пробег. Их необходимо сохранить в атрибуты экземпляра name, max_speed и mileage соответственно
метод display_info , который печатает информацию в следующем виде:
Vehicle Name: {name}, Speed: {max_speed}, Mileage: {mileage}
Затем создайте подкласс Bus , унаследованный от Vehicle. Оставьте его пустым'''

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')

class Bus(Vehicle):
    pass
