
'''Создайте класс Dog, у которого есть:

метод __init__, принимающий имя и возраст собаки и сохраняющий их в аргументы name и age
метод description, который возвращает строку в виде «{name} is {age} years old»
метод speak принимающий один аргумент, который возвращает строку вида «{name} says {sound}»'''

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

jack = Dog("Jack", 4)

print(jack.description())
print(jack.speak("Woof Woof"))