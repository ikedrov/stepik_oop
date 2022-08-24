'''Создайте класс Date, у которого есть:

конструктор __init__, принимающий 3 аргумента: день, месяц и год.
свойство date , которое возвращает строку определенного формата "<день>/<месяц>/<год>";
свойство usa_date, которое возвращает строку определенного формата "<месяц>-<день>-<год>";'''

class Date:

    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    @property
    def date(self):
        return f'{self.day:02}/{self.month:02}/{self.year:04}'

    @property
    def usa_date(self):
        return f'{self.month:02}-{self.day:02}-{self.year:04}'

d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date)
print(d1.usa_date)
print(d2.date)
print(d2.usa_date)