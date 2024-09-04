from random import randint


class Pokemon:
    def __init__(self, name, element, hp, atk, dev, spd, ability):
        self.__name = name
        self.__element = element
        self.__hp = int(hp) + randint(0, 32)
        self.__atk = int(atk) + randint(0, 32)
        self.__dev = int(dev) + randint(0, 32)
        self.__spd = int(spd) + randint(0, 32)
        self.__ability = ability

    def roll_accuracy(self):
        hit = randint(1, 101)
        return hit <= self.__ability.accuracy

    def damage(self):
        return self.__atk + self.__ability.power

    def defend(self, base_dmg):
        hit_dmg = max(0, base_dmg - self.__dev)
        self.__hp -= hit_dmg
        print(f'-{hit_dmg} hp')
        print(f'Current hp:{self.__hp}')

    def fainted(self):
        return self.__hp <= 0

    def speed(self):
        return self.__spd

    def __repr__(self):
        return (f'{self.__name}, {self.__element}, {self.__hp},'
                f' {self.__atk}, {self.__dev}, {self.__spd}, {self.__ability}')


