'''Нам необходимо создать класс Building. Мы должны научиться создавать здание определенной этажности и уметь бронировать за компанией определенный этаж в здании. Важно, что в нашем классе за одним этажом может быть закреплена только одна компания

Для этого в классе Building должно быть реализованы

метод __init__, который принимает количество этажей в здании
метод __setitem__, который закрепляет за определенным этажом компанию. Если этаж был занят другой компанией, нужно заменить название другой компанией
метод __getitem__, который возвращает название компании с этого этажа. В случае, если этаж пустует, следует вернуть None
метод __delitem__, который высвобождает этаж'''

class Building:
    def __init__(self, height):
        self.height = height
        self.offices = {key: None for key in range(height)}

    def __setitem__(self, key, value):
        if 0 <= key <= self.height:
            self.offices[key] = value
        else:
            raise IndexError('Floor is not in building')

    def __getitem__(self, item):
        if 0 <= item <= self.height:
            return self.offices[item]

    def __delitem__(self, key):
        if 0 <= key <= self.height:
            self.offices[key] = None

iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])
