'''
Для этого нам понадобится реализовать несколько классов и связать их между собой. Первый класс, который мы реализуем, будет Product. Это класс, описывающий товар. В нем должно быть реализовано:

метод __init__, принимающий на вход имя товара и его стоимость. Эти значения необходимо сохранить в атрибутах name и price
'''
'''
Далее для оформления заказа нам нужен пользователь. Для этого создадим класс User, который содержит:

метод __init__, принимающий на вход логин пользователя и необязательный аргумент баланс его счета(по умолчанию 0). Логин необходимо сохранить в атрибуте login , а баланс необходимо присвоить сеттеру   balance  (см. пункт 4)
метод __str__, возвращающий строку вида «Пользователь {login}, баланс - {balance}»
Cвойство геттер balance, которое возвращает значение self.__balance;
Свойство сеттер balance, принимает новое значение баланса и устанавливает его в атрибут self.__balance ;
метод deposit  принимает числовое значение и прибавляет его к атрибуту self.__balance ;
метод payment  принимает числовое значение, которое должно списаться с баланса пользователя. Если на счете у пользователя не хватает средств, то необходимо вывести фразу  «Не хватает средств на балансе. Пополните счет» и вернуть False. Если средств хватает, списываем с баланса у пользователя указанную сумму и возвращаем True'''

'''
Последний штрих - создание класса корзины, куда наш пользователь будет складывать товары. Для этого нам понадобятся ранее созданные классы User и Product

И так, создаем класс Cart, который содержит:

метод __init__, принимающий на вход экземпляр класса User . Его необходимо сохранить в атрибуте user . Помимо этого метод  должен создать атрибут goods - пустой словарь (лучше использовать defaultdict). Он нужен будет для хранения наших товаров и их количества(ключ словаря - товар, значение - количество). И еще нам понадобится создать защищенный атрибут .__total со значением 0. В нем будет хранится итоговая сумма заказа
метод add принимает на вход экземпляр класса Product и необязательный аргумент количество товаров (по умолчанию 1). Метод add  должен увеличить в корзине (атрибут goods) количество указанного товара  на переданное значение количество и пересчитать атрибут self.__total
метод remove  принимает на вход экземпляр класса Product и необязательный аргумент количество товаров (по умолчанию 1).  Метод remove  должен уменьшить в корзине (атрибут goods) количество указанного товара  на переданное значение количество и пересчитать атрибут self.__total. Обратите внимание на то, что количество товара в корзине не может стать отрицательным как и итоговая сумма
Cвойство геттер total  , которое возвращает значение self.__total;
метод order  должен использовать метод payment  из класса User и передать в него итоговую сумму корзины. В случае, если средств пользователю хватило, вывести сообщение «Заказ оплачен», в противном случае - «Проблема с оплатой»;
метод print_check  печатающий на экран чек. Он должен начинаться со строки
---Your check---
Затем выводится состав корзины в алфавитном порядке по названию товара в виде
{Имя товара} {Цена товара} {Количество товара} {Сумма} 
И заканчивается чек строкой
---Total: {self.total}---'''


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, login, balance = 0):
        self.login = login
        self.__balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value:int):
        self.__balance = value

    def deposit(self, value:int):
        self.__balance += value

    def payment(self, value):
        if self.__balance < value:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.__balance -= value
            return True

class Cart:
    def __init__(self, User):
        self.user = User
        self.goods = dict()
        self.__total = 0

    def add(self, product, amount = 1):
        self.goods[product] = self.goods.get(product, 0) + amount
        self.__total += amount * product.price

    def remove(self, product, amount=1):
        if self.goods[product] < amount:
            self.__total -= product.price * (amount - (amount - self.goods.get(product, 0)))
            del self.goods[product]
        else:
            self.__total -= amount * product.price
            self.goods[product] = self.goods.get(product, 0) - amount
    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        for k, v in sorted(self.goods.items(), key = lambda x: x[0].name):
            print(k.name, k.price, v, k.price * v)
        print(f'---Total: {self.total}---')

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
cart_billy.add(lemon, 3)
cart_billy.print_check()
cart_billy.remove(lemon, 6)
cart_billy.print_check()
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
cart_billy.order()
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20

