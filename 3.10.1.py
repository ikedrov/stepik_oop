'''Создайте класс PowerTwo, который возвращает следующую степень двойки, начиная с нулевой степени (20=1). Внутри класса реализуйте:

метод __init__. Он должен принимать одно положительное число - степень двойки, до которой нужно итеририроваться включительно (см пример ниже)
методы __iter__ и __next__ для итерирования по степеням двойки'''

class PowerTwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num <= self.max:
            res = 2 ** self.num
            self.num += 1
            return res
        else:
            raise StopIteration

for i in PowerTwo(4):
    print(i) # итерируемся до 4й степени двойки