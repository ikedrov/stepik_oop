'''Создайте класс Registration, который пока будет проверять только введенный логин. Под логином мы будем подразумевать почту пользователя, поэтому необходимо будет сделать некоторые проверки.

В классе Registration необходимо реализовать:

метод __init__ принимающий один аргумент логин пользователя. Метод __init__ должен сохранить переданный логин через сеттер (см пункт 3). То есть когда отработает данный код
def __init__(self, логин):
    self.login = логин # передаем в сеттер login значение логин
должно сработать свойство сеттер login из пункта 3 для проверки валидности переданного значения

Cвойство геттер login, которое возвращает значение self.__login;
Свойство сеттер login, принимает значение нового логина. Новое значение мы должны проверить на следующее:
логин, так как является почтой, должен содержать один символ собаки «@». В случае, если в логине отсутствует символ «@», вызываем исключение при помощи строки raise ValueError("Логин должен содержать один символ '@'")
логин должен содержать символ точки «.» после символа «@».В случае, если после @ нету точки, вызываем исключение при помощи строки raise ValueError("Логин должен содержать символ '.'")
Если значение проходит проверку новое значение логина сохраняется в атрибут self.__login'''
class Registration:

    def __init__(self, login):
        self.login = login

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value:str):
        if '@' not in value:
            raise ValueError("Логин должен содержать один символ '@'")
        if '.' in value:
            if value.index('@') > value.index('.'):
                raise ValueError("Логин должен содержать символ '.'")
        else:
            raise ValueError("Login must include at least one ' @ '")
        self.__login = value

