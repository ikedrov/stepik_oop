'''Ваша задача  создать класс CustomLabel, у которого есть:

метод __init__, принимающий один обязательный аргумент текст виджета, его необходимо сохранить в атрибут text. И также в метод  может поступать произвольное количество именованных аргументов. Их необходимо сохранять в атрибуты экземпляра под тем же названием
метод config, который принимает произвольное количество именованных атрибутов. Он должен создать атрибут с указанным именем или, если этот атрибут уже присутствовал в экземпляре, изменить его на новое значение'''

class CustomLabel:

    def __init__(self, text, **kwargs):
        self.text = text
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def config(self, **kwargs):
        self.__dict__.update(kwargs)


label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')

print(label.__dict__)

label.config(color='red', bd=100)

print(label.__dict__)
