'''
Создайте базовый класс User, у которого есть:

метод __init__, принимающий имя пользователя и его роль. Их необходимо сохранить в атрибуты экземпляра name и role соответственно
Затем создайте класс Access , у которого есть:

приватный атрибут класса __access_list , в котором хранится список ['admin', 'developer']
приватный статик-метод __check_access , который принимает название роли и возвращает True, если роль находится в списке __access_list , иначе - False
публичный статик-метод get_access , который должен принимать экземпляр класса User и проверять есть ли доступ у данного пользователя к ресурсу при помощи метода __check_access  . Если у пользователя достаточно прав, выведите на экран сообщение «User <name>: success», если прав недостаточно - «AccessDenied». Если передается тип данных отличный от экземпляр класса Userнеобходимо вывести сообщение «AccessTypeError»
'''

class User:

    def __init__(self, name, role):
        self.name = name
        self.role = role

class Access:

    __access_list = ['admin', 'developer']

    def __check_access(User):
        return User.role in Access.__access_list

    @staticmethod
    def get_access(usr):
        if isinstance(usr, User):
            if Access.__check_access(usr):
                print(f'User {usr.name}: success')
            else:
                print('AccessDenied')
        else:
            print('AccessTypeError')

user1 = User('batya99', 'admin')
Access.get_access(user1)
