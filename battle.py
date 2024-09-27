import random
from pokemonteam import PokemonTeam
from pokemonlist import POKEMON_ATTACK_VALUES


class Battle:
    def __init__(self, enemy_active_pokemon, player_active_pokemon, player_pokemon_team):
        self.enemy_pokemon = enemy_active_pokemon
        self.player_pokemon = player_active_pokemon
        self.player_pokemon_team = player_pokemon_team

    def start_battle(self, enemy_active_pokemon, player_active_pokemon):
        print(f'Enemy Pokemon: {enemy_active_pokemon.get_name()} ')
        print(f'Player Pokemon: {player_active_pokemon.get_name()} ')

    def roll_speed(self):
        pass

    def check_fainted(self, player_active_pokemon, enemy_active_pokemon):
        if player_active_pokemon.get_current_hp() <= 0:
            print('Your Pokemon fainted.. ')
            self.switch()
            return True
        elif enemy_active_pokemon.get_current_hp() <= 0:
            print('Enemy Pokemon fainted!! ')
            return True
        else:
            return False

    def attack_selection(self, player_active_pokemon, enemy_active_pokemon):
        abilities = player_active_pokemon.get_ability_list()
        while True:
            if len(abilities) > 1:
                choice = int(input(f'choose your attack: {abilities} (1-{len(abilities)}) '))
                if choice < 1 or choice > len(abilities):
                    print('Ability not avalible ')
                else:
                    ability = player_active_pokemon.get_ability_list()[choice - 1]
                    print(ability)
                    self.attack_enemy(player_active_pokemon, enemy_active_pokemon, ability)
                    break

    def enemy_turn(self, player_active_pokemon, enemy_active_pokemon):
        random_ability = random.choice(enemy_active_pokemon.get_ability_list())
        print(random_ability)
        self.attack_player(player_active_pokemon, enemy_active_pokemon, random_ability)

    def bag(self):
        pass

    def switch(self, player_pokemon_team, player_active_pokemon):
        print('Which Pokemon should be send in? ')
        team_number = int(input(f'{player_pokemon_team} )'))
        player_active_pokemon = player_pokemon_team[0]

    def flee(self, player_active_pokemon, enemy_active_pokemon):
        if player_active_pokemon.get_speed() >= enemy_active_pokemon.get_speed():
            print('You escaped succesfully ')
            return True
        elif player_active_pokemon.get_speed() <= enemy_active_pokemon.get_speed():
            print('You could´nt escape ')
            return False

    def display_actions(self, player_active_pokemon, enemy_active_pokemon, player_pokemon_team):
        print(f'{player_active_pokemon.get_name()} (HP: {player_active_pokemon.get_current_hp()}) '
              f'vs {enemy_active_pokemon.get_name()} (HP: {enemy_active_pokemon.get_current_hp()}) ')
        print('Choose an action: ')
        selection = input('1. Attack , 2. Switch, 3. Bag, 4. Flee ')
        if selection == '1':
            self.attack_selection(player_active_pokemon, enemy_active_pokemon)
        elif selection == '2':
            self.switch(player_pokemon_team, player_active_pokemon)
        elif selection == '3':
            self.bag()
        elif selection == '4':
            self.flee(player_active_pokemon, enemy_active_pokemon)

    def attack_enemy(self, player_active_pokemon, enemy_active_pokemon, ability):
        damage = player_active_pokemon.get_atk() * (0.01 * (int(POKEMON_ATTACK_VALUES[ability]['Attack_Strength']))) / (1 + (enemy_active_pokemon.get_defense() / 200))
        damage = int(max(1, player_active_pokemon.get_max_hp() * 0.5))
        enemy_active_pokemon.take_damage(damage)
        print(f'{player_active_pokemon.get_name()} attacked {enemy_active_pokemon.get_name()} for {damage} damage! ')
        print(f'{enemy_active_pokemon.get_name()} has {enemy_active_pokemon.get_current_hp()} HP left ')

    def attack_player(self, player_active_pokemon, enemy_active_pokemon, ability):
        damage = enemy_active_pokemon.get_atk() * (0.01 * (int(POKEMON_ATTACK_VALUES[ability]['Attack_Strength']))) / (1 + (player_active_pokemon.get_defense() / 200))
        damage = int(max(1, enemy_active_pokemon.get_max_hp() * 0.5))
        player_active_pokemon.take_damage(damage)
        print(f'{enemy_active_pokemon.get_name()} attacked {player_active_pokemon.get_name()} for {damage} damage! ')
        print(f'{player_active_pokemon.get_name()} has {player_active_pokemon.get_current_hp()} HP left ')
