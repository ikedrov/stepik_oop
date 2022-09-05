'''Создайте класс  File, у которого есть:

метод __init__, который должен принимать на вход имя файла и записывать его в атрибут name. Также необходимо создать атрибуты in_trash , is_deleted  и записать в них значение False
метод  restore_from_trash, который печатает фразу «Файл {name} восстановлен из корзины» и проставляет атрибут in_trash в значение False
метод  remove, который печатает фразу «Файл {name} был удален» и проставляет атрибут is_deleted  в значение True
метод read, который
печатает фразу «ErrorReadFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
печатает фразу «ErrorReadFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
печатает фразу «Прочитали все содержимое файла {self.name}» если файл не удален и не в корзине
метод write, который принимает значение content для записи и
печатает фразу «ErrorWriteFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
печатает фразу «ErrorWriteFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
печатает фразу «Записали значение {content} в файл {self.name}», если файл не удален и не в корзине
Далее создайте класс  Trash у которого есть:

атрибут класса  content изначально равный пустому списку
статик-метод  add, который принимает файл и сохраняет его в корзину: для этого нужно добавить его в атрибут content и проставить файлу атрибут in_trash значение True. Если в метод add передается не экземпляр класса File, необходимо вывести сообщение «В корзину добавлять можно только файл»
статик-метод  clear, который запускает процесс очистки файлов в корзине. Необходимо для всех файлов, хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла remove. Атрибут content  после очистки должен стать пустым списком. Сама процедура очистки должна начинаться фразой «Очищаем корзину» и заканчиваться фразой «Корзина пуста»
статик-метод  restore, который запускает процесс восстановления файлов из корзины. Необходимо для всех файлов, хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла restore_from_trash. Атрибут content  после очистки должен стать пустым списком. Сама процедура восстановления должна начинаться фразой «Восстанавливаем файлы из корзины» и заканчиваться фразой «Корзина пуста»'''

class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
        else:
            print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
        else:
            print(f'Записали значение {content} в файл {self.name}')

class Trash:
    content = []

    @staticmethod
    def add(file):
        if isinstance(file, File):
            Trash.content.append(file)
            File.in_trash = True
        else:
            print('В корзину добавлять можно только файл')

    @staticmethod
    def clear():
        print('Очищаем корзину')
        while Trash.content:
            Trash.content.pop(0).remove()
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        while Trash.content:
            File.restore_from_trash(Trash.content.pop(0))
        print('Корзина пуста')
