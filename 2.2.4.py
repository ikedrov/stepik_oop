'''Создайте класс Zebra, внутри которого есть метод which_stripe , который поочередно печатает фразы "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"'''

class Zebra:
    def __init__(self, color = 0):
        self.color = color

    def which_stripe(self):
        self.color += 1
        if self.color % 2 == 1:
            print('Полоска белая')
        else:
            print('Полоска черная')

z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()

