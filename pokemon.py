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

    def damage(self):
        return self.__atk + self.__ability.power

    def roll_attack(self):
        result = randint(1, 101)
        return result <= self.__ability.accuracy

    def defend(self, base_dmg):
        hit_dmg = max(0, base_dmg - self.__dev)
        self.__hp -= hit_dmg
        print(f'-{hit_dmg} HP')
        print(f'{self.__name} current HP: {self.__hp}')

    def fainted(self):
        print(f'{self.__name} fainted... ')
        return self.__hp <= 0

    def get_name(self):
        return self.__name

    def __repr__(self):
        return (f'{self.__name}, {self.__element}, HP: {self.__hp}, '
                f'ATK: {self.__atk}, DEF: {self.__dev}, SPD: {self.__spd},'
                f'Abilities: {self.__ability}')

#    def __repr__(self):
#        return self.__name, self.__element, self.__hp, self.__atk, self.__dev, self.__spd, self.__ability

