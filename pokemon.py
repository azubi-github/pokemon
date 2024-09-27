from random import randint
import random

from pokemonlist import POKEMON_ATTACK


class Pokemon:
    def __init__(self, name, element, hp, atk, dev, spd):
        self.__name = name
        self.__element = element
        self.__hp = int(hp) + randint(0, 32)
        self.__atk = int(atk) + randint(0, 32)
        self.__dev = int(dev) + randint(0, 32)
        self.__spd = int(spd) + randint(0, 32)
        self.__current_hp = self.__hp
        self.__ability = self.set_ability_list()

    def get_speed(self):
        return self.__spd

    def take_damage(self, damage):
        self.__current_hp = self.__current_hp - damage

    def get_defense(self):
        return self.__dev

    def get_current_hp(self):
        return self.__current_hp

    def get_max_hp(self):
        return self.__hp

    def get_atk(self):
        return self.__atk

    def get_name(self):
        return self.__name

    def get_ability_list(self):
        return self.__ability

    def set_ability_list(self):
        ability_list = []
        for x in range(3):
            choice = random.choice(list(POKEMON_ATTACK[self.__element]))
            if choice in ability_list:
                while choice in ability_list:
                    choice = random.choice(list(POKEMON_ATTACK[self.__element]))
                ability_list.append(choice)
            else:
                ability_list.append(choice)
        ability_list.append(random.choice(list(POKEMON_ATTACK["Normal"])))
        return ability_list

    def random_ability(self):
        chosen_ability = random.choice(self.__ability)
        return chosen_ability

    def __repr__(self):
        return (f'{self.__name}, {self.__element}, HP: {self.__hp}, '
                f'ATK: {self.__atk}, DEF: {self.__dev}, SPD: {self.__spd},'
                f'Abilities: {self.__ability}')
