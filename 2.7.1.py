'''Создайте класс Notebook, у которого есть:

конструктор __init__, принимающий 1 аргумента: список записей, в принципе там могут быть любые значения. Необходимо сохранить его в защищенном атрибуте ._notes
свойство notes_list, которое распечатает содержимое атрибута ._notes в виде упорядоченного списка '''

class Notebook:

    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        for i, j in enumerate(self._notes, 1):
            print(f'{i}.{j}')

note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list