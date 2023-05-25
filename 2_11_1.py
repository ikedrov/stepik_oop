'''
Создайте класс BankAccount, который имеет:

атрибут класса bank_name со значением "Tinkoff Bank"
 
атрибут класса address со значением  "Москва, ул. 2-я Хуторская, д. 38А"
 
метод __init__, который устанавливает значения атрибутов name и balance : владелец счета и значение счета
 
класс метод create_account, который возвращает новый экземпляр класса BankAccount. Метод принимает имя клиента и сумму взноса
 
класс метод bank_info, который возвращает информация о банке в виде:
«{bank_name} is located in {address}»
'''

class BankAccount:

    bank_name = 'Tinkoff Bank'
    address = 'Москва, ул. 2-я Хуторская, д. 38А'

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, balance):
        new_acc = cls(name, balance)
        return new_acc

    @classmethod
    def bank_info(cls):
        return f'{cls.bank_name} is located in {cls.address}'