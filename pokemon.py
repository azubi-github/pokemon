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
        self.__current_hp = self.__hp
        self.__ability = ability

    def get_speed(self):
        return self.__spd

    def attack_enemy(self, enemy_active_pokemon, player_active_pokemon):
        damage = self.__atk - enemy_active_pokemon.get_defense()
        damage = int(max(0, damage))
        enemy_active_pokemon.take_damage(damage)
        print(f'{player_active_pokemon.get_name()} attacked {enemy_active_pokemon.get_name()} for {damage} damage! ')
        print(f'{enemy_active_pokemon.get_name()} has {enemy_active_pokemon.get_current_hp()} HP left ')

    def attack_player(self, player_active_pokemon, enemy_active_pokemon):
        damage = self.__atk - player_active_pokemon.get_defense()
        damage = int(max(0, damage))
        player_active_pokemon.take_damage(damage)
        print(f'{enemy_active_pokemon.get_name()} attacked {player_active_pokemon.get_name()} for {damage} damage! ')
        print(f'{player_active_pokemon.get_name()} has {player_active_pokemon.get_current_hp()} HP left ')

    def take_damage(self, damage):
        self.__current_hp = self.__current_hp - damage

    def get_defense(self):
        return self.__dev

    def get_current_hp(self):
        return self.__current_hp

    def get_name(self):
        return self.__name

    def __repr__(self):
        return (f'{self.__name}, {self.__element}, HP: {self.__hp}, '
                f'ATK: {self.__atk}, DEF: {self.__dev}, SPD: {self.__spd},'
                f'Abilities: {self.__ability}')

