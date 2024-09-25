from random import randint
import abilities
import battle


class Pokemon:
    def __init__(self, name, element, hp, atk, dev, spd, ability):
        self.__name = name
        self.__element = element
        self.__hp = int(hp) + randint(0, 32)
        self.__atk = int(atk) + randint(0, 32)
        self.__dev = int(dev) + randint(0, 32)
        self.__spd = int(spd) + randint(0, 32)
        self.__current_hp = self.__hp
        self.__ability = ability

    def get_speed(self):
        return self.__spd

    def take_damage(self, damage):
        self.__current_hp = self.__current_hp - damage

    def get_defense(self):
        return self.__dev

    def get_current_hp(self):
        return self.__current_hp

    def get_atk(self):
        return self.__atk

    def get_name(self):
        return self.__name

    def __repr__(self):
        return (f'{self.__name}, {self.__element}, HP: {self.__hp}, '
                f'ATK: {self.__atk}, DEF: {self.__dev}, SPD: {self.__spd},'
                f'Abilities: {self.__ability}')

print('test')
