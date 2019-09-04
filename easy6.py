# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# class Cars :
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print('машина поехала')
#
#     def stop(self):
#         print('машина остановилась')
#
#     def turnleft(self):
#         print('машина поворачивает на лево')
#
#     def turnright(self):
#             print('машина поворачивает на право')



# class TownCar:
#     def __init__(self, speed, color, name, is_police):
#             self.speed = speed
#             self.color = color
#             self.name = name
#             self.is_police = is_police
#     def go(self):
#                 print('Машина едит со скоростью {}'.format(self.color))
#                 towncar = TownCar('300', 'Желтый', 'бугати', 1)
#
#
class towncar:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

        def go(self):
            print('машина поехала')

        def stop(self):
            print('машина поехала')

        def turn(self):
            print('машина поехала')


class sportcar:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

        def go(self):
            print('машина поехала')

        def stop(self):
            print('машина поехала')

        def turn(self):
            print('машина поехала')


class workcar:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

        def go(self):
            print('машина поехала')

        def stop(self):
            print('машина поехала')

        def turn(self):
            print('машина поехала')


class Policecar:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

        def go(self):
            print('машина поехала')

        def stop(self):
            print('машина поехала')

        def turn(self):
            print('машина поехала')
    #

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

auto=towncar('ford',120,'red',0,)

print(auto.name,auto.speed,auto.color,auto.is_police)

auto.go