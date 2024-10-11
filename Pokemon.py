from random import randint
import random

from Ability import Ability
from pokemonlist import POKEMON_ATTACK, ELEMENT_TYPE, POKEMON_ATTACK_VALUES

class Pokemon:
    """Erstellt ein Pokemon mit der übergabe von Name, Element, HP, ATK, DEV und SPD"""
    def __init__(self, name, element, health, attack, defense, speed):
        self.__name = name
        self.__element = str(element)
        self.__hp = int(health) + randint(0, 32)
        self.__atk = int(attack) + randint(0, 32)
        self.__dev = int(defense) + randint(0, 32)
        self.__spd = int(speed) + randint(0, 32)
        self.__current_hp = self.__hp
        self.__ability, self.__ability_names = self.set_ability_list()
        self.__fainted = False

    def get_pokemon(self):
        return (self.__name, self.__element, self.__hp, self.__atk, self.__dev, self.__spd, self.__current_hp,
                self.__ability, self.__fainted)

    def get_speed(self):
        return self.__spd

    def get_element(self):
        return self.__element

    def take_damage(self, damage):
        self.__current_hp = self.__current_hp - damage

    def healing(self, heal_amount):
        self.__current_hp = self.__current_hp + heal_amount
        healed_amount = heal_amount
        if self.__current_hp > self.__hp:
            healed_amount = self.__current_hp - self.__hp
            self.__current_hp = self.__hp
        print(f"Your {self.__name} got healed by {healed_amount}")

    def get_defense(self):
        return self.__dev

    def get_current_hp(self):
        return self.__current_hp

    def get_ability_name(self, ability):
        return ability.get_name()

    def get_ability_attack_strength(self, ability):
        return ability.get_attack_strength()

    def get_ability_accruacy(self, ability):
        return ability.get_accuracy()

    def get_ability_element(self, ability):
        return ability.get_element()

    def get_max_hp(self):
        return self.__hp

    def get_atk(self):
        return self.__atk

    def get_name(self):
        return self.__name

    def get_ability_list(self):
        return self.__ability

    def get_ability_name_list(self):
        return self.__ability_names

    def set_ability_list(self):
        ability_list = []
        ability_name_list = []
        for x in range(3):
            choice = random.choice(list(POKEMON_ATTACK[self.__element].keys()))
            if choice in ability_name_list:
                while choice in ability_name_list:
                    choice = random.choice(list(POKEMON_ATTACK[self.__element].keys()))
                ability_name_list.append(choice)
            else:
                ability_name_list.append(choice)
        random_normal_ability = random.choice(list(POKEMON_ATTACK["Normal"].keys()))
        if random_normal_ability in ability_name_list:
            while random_normal_ability in ability_name_list:
                random_normal_ability = random.choice(list(POKEMON_ATTACK["Normal"].keys()))
        else:
            ability_name_list.append(random_normal_ability)
        for i in ability_name_list:
            i = Ability(name=i, **POKEMON_ATTACK_VALUES[i])
            ability_list.append(i)
        return ability_list, ability_name_list

    def random_ability(self):
        chosen_ability = random.choice(self.__ability)
        return chosen_ability

    def hitchance(self, ability_accuracy):
        hitroll = random.randint(1, 101)
        if hitroll > ability_accuracy:
            return "miss"
        elif ability_accuracy > hitroll:
            if hitroll > 15:
                return "hit"
            else:
                return "crit"

    def is_fainted(self):
        if self.__current_hp <= 0:
            self.__fainted = True
        return self.__fainted

    def element_abfrage(self, enemy_element, ability):
        multip = ELEMENT_TYPE[ability.get_element()][enemy_element.get_element()]
        print(multip)
        return multip

    def __repr__(self):
        return (f'{self.__name}, {self.__element}, HP: {self.__hp}, '
                f'ATK: {self.__atk}, DEF: {self.__dev}, SPD: {self.__spd},'
                f'Abilities: {self.__ability}')
