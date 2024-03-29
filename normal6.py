# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
#
# class Person:
#     def __init__(self, name, power, color):
#         self.name = name
#         self.power = power
#         self.color = color
#
# class Player (Person):
class Person:

        def __init__(self, name, health, armor, damage):
            self.name = name
            self.health = health
            self.armor = armor
            self.damage = damage

        def calculate_damage(self, enemy):
            return self.damage / enemy.armor

        def attack(self, enemy):
            enemy.health -= self.calculate_damage(enemy)

class Player(Person):
        pass

class Enemy(Person):
    pass

class Game:

        def __init__(self, player, enemy):
            self._player = player
            self._enemy = enemy

        def start(self):
            last_attacker = self._player
            while self._player.health > 0 and self._enemy.health > 0:
                if last_attacker == self._player:
                    self._enemy.attack(self._player)
                    last_attacker = self._enemy
                else:
                    self._player.attack(self._enemy)
                    last_attacker = self._player
            if player.health > 0:
                print('Player win.')
            else:
                print('Enemy win.')

player = Player('Bob', 100, 1.2, 10)
enemy = Enemy('John', 100, 1.1, 10)
game = Game(player, enemy)

game.start()
