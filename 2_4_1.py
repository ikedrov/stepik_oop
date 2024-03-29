'''
Предположим, у нас есть класс WeatherStation для метеостанции, которая собирает данные с нескольких датчиков. Каждый экземпляр датчика можно создать отдельно, но вы все равно хотите поддерживать единое состояние для всей метеостанции. Для этого можно использовать шаблон Моносостояния, имея общее состояние для всех экземпляров класса датчика.

Датчики будут измерять температуру, влажность и давление. Ваша задача определить класс WeatherStation, у которого

имеются разделяемые атрибуты temperature, humidity и pressure. Вот их начальные состояния:
{"temperature": 0, "humidity": 0, "pressure": 0}
метод update_data, который изменяет состояние сразу трех показаний.
 
метод get_current_data, который возвращает кортеж показаний  temperature, humidity и pressure'''

class WeatherStation:

    __shared_attr = {'temperature': 0, 'humidity': 0, 'pressure': 0}

    def __init__(self):
        self.__dict__ = WeatherStation.__shared_attr

    def update_data(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def get_current_data(self):
        return tuple(self.__dict__.values())