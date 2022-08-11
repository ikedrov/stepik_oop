'''В предыдущей задачи вы могли обратить внимание на то, что выводится всегда одно и тоже имя робота в методе say_hello . Давайте это исправим при помощи атрибута экземпляра name . Для этого переопределяем класс Robot, в котором должны быть реализованы

метод set_name , принимающий имя робота и сохраняющий его в атрибуте экземпляра name
метод say_hello , Метод должен проверить, если у ЭК атрибут name . Если атрибут name  присутствует, необходимо напечатать фразу «Hello, human! My name is <name>». Если атрибут name  отсутствует у экземпляра, печатайте сообщение «У робота нет имени»
метод say_bye ,  печатающий на экран фразу «See u later alligator»'''

class Robot:
    def set_name(self, name):
        self.name = name

    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')


