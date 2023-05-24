'''
Необходимо создать приложение для учета задач, которое будет использовать классы Task, TaskList и TaskManager.

 

Класс Task будет хранить информацию о задаче (название, описание, статус выполнения), состоит из: 

метода __init__, принимающий  и сохраняет в атрибуты экземпляра name , description и status. По умолчанию status равен False.
 
метод display , который печатает информацию в следующем виде:
​​​​​{название задачи} (Сделана/Не сделана)
В зависимости от статуса задачи выводится Сделана или Не сделана 
 

Класс TaskList будет содержать список задач и методы для добавления/удаления задач, состоит из:

метода __init__, который должен создать пустой список задач в атрибуте tasks
 
метода add_task, который принимает задачу и добавляет ее в конец списка задач
 
метода remove_task, который принимает задачу и удаляет ее из списка задач
 

Класс TaskManager будет содержать методы для отображения списка задач и изменения статуса выполнения задач. В нем должно быть реализовано:

метод __init__, который должен принимать экземпляр TaskList  и сохранять его в атрибуте  task_list
 
метод  mark_done, который принимает задачу (экземпляр Task)  и устанавливает ей истинный статус выполнения
 
метод  mark_undone, который принимает задачу (экземпляр Task)  и устанавливает ей ложный статус выполнения
 
метод  show_tasks, который для каждой хранящейся задачи в списке вызывает метод display
'''

class Task:

    def __init__(self, name, description, status = False):
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        if self.status == True:
            print(self.name, '(Сделана)')

        else:
            print(self.name, '(Не сделана)')

class TaskList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

class TaskManager:

    def __init__(self, TaskList):
        self.task_list = TaskList

    def mark_done(self, Task):
        Task.status = True

    def mark_undone(self, Task):
        Task.status = False

    def show_tasks(self):
        for i in self.task_list.tasks:
            Task.display(i)