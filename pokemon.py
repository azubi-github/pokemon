from random import randint
import abilities


class Pokemon:
    def __init__(self, name, element, hp, atk, dev, spd, ability):
        self.__name = name
        self.__element = element
        self.__hp = int(hp) + randint(0, 32)
        self.__atk = int(atk) + randint(0, 32)
        self.__dev = int(dev) + randint(0, 32)
        self.__spd = int(spd) + randint(0, 32)
        self.__ability = ability

    def get_speed(self):
        return self.__spd

    def attack_enemy(self, enemy_active_pokemon):
        damage = self.__atk - enemy_active_pokemon.get_defense()
        damage = (0, damage)
        enemy_active_pokemon.take_damage(damage)
        print(f'{self.__name} attacked {enemy_active_pokemon.get_name()} for {damage} damage! ')

    def attack_player(self, player_active_pokemon):
        damage = self.__atk +  - player_active_pokemon.get_defense()
        damage = (0, damage)
        player_active_pokemon.take_damage(damage)
        print(f'{self.__name} attacked {player_active_pokemon.get_name()} for {damage} damage! ')

    def take_damage(self, damage):
        self.__hp -= max(0, damage)
        print(f'{self.__name} has {self.__hp} HP left ')

    def get_defense(self):
        return self.__dev

    def get_hp(self):
        return self.__hp

    def get_name(self):
        return self.__name

    def __repr__(self):
        return (f'{self.__name}, {self.__element}, HP: {self.__hp}, '
                f'ATK: {self.__atk}, DEF: {self.__dev}, SPD: {self.__spd},'
                f'Abilities: {self.__ability}')

