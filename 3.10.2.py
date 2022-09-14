'''Создайте класс InfinityIterator, который реализует бесконечный итератор, который будет при каждой новой итерации или вызовы функции next будет возвращать число, увеличенное на 10 от предыдущего значения. Начинать нужно с нуля.'''

class InfinityIterator:
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        x = self.num
        self.num += 10
        return x