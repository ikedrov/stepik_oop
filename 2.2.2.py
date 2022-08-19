'''Создайте класс Laptop, у которого есть:

конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука. На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price и также атрибут laptop_name - строковое значение, следующего вида: "<brand> <model>"'''

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'

laptop1 = Laptop('hp', '11', 10000)
laptop2 = Laptop('hp', '222', 11000)

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price)
print(hp.laptop_name)