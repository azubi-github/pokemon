from pokemonlist import POKEMON_ATTACK_VALUES
from Pokemonteam import PokemonTeam


class Battle:
    def __init__(self, enemy_active_pokemon, player_active_pokemon, enemy_team, player_team):
        self.enemy_pokemon = enemy_active_pokemon
        self.player_pokemon = player_active_pokemon
        self.enemy_team = enemy_team
        self.player_team = player_team

    def start_battle(self, enemy_active_pokemon, player_active_pokemon):
        print(f'Enemy Pokemon: {enemy_active_pokemon.get_name()} ')
        print(f'Player Pokemon: {player_active_pokemon.get_name()} ')

    def check_player_fainted(self, player_active_pokemon, player_team):
        if player_active_pokemon.get_current_hp() <= 0:
            print(f'Your {player_active_pokemon.get_name()} fainted.. ')
            if player_active_pokemon.get_current_hp() <= 1000:
                print(f'Sorry buddy... your {player_active_pokemon.get_name()} got blasted out of existence...')
                if player_team.get_team_len > 1:
                    player_active_pokemon = player_team.switch(player_active_pokemon, player_team)
        return player_active_pokemon

    def check_enemy_fainted(self, enemy_active_pokemon, enemy_team):
        if enemy_active_pokemon.get_current_hp() <= 0:
            print(f'{enemy_active_pokemon.get_name()} fainted.. ')
            if enemy_active_pokemon.get_current_hp() <= 1000:
                print(f'You blasted {enemy_active_pokemon.get_name()} out of existence!')
                if enemy_team.get_team_len() > 1:
                    # PokemonTeam.enemy_switch(enemy_active_pokemon, enemy_team)
                    pass

    def attack_selection(self, player_active_pokemon, enemy_active_pokemon):
        abilities = player_active_pokemon.get_ability_list()
        print('Choose an Ability: ')
        for i, ability in enumerate(abilities):
            print(f'{i + 1}. {ability}')

        while True:
            try:
                choice = int(input(f'choose your attack: {abilities} (1-{len(abilities)}) ')) - 1
                if choice > 1 or choice > len(abilities):
                    print('Invalid selection ')
                else:
                    ability = player_active_pokemon.get_ability_list()[choice]
                    print(f'{player_active_pokemon.get_name()} uses {ability}')
                    self.attack_enemy(player_active_pokemon, enemy_active_pokemon, ability)
            except ValueError:
                print('Please enter a number ')
            break

    def enemy_turn(self, player_active_pokemon, enemy_active_pokemon):
        self.attack_player(player_active_pokemon, enemy_active_pokemon)

    def bag(self):
        pass

    def flee(self, player_active_pokemon, enemy_active_pokemon):
        if player_active_pokemon.get_speed() >= enemy_active_pokemon.get_speed():
            print('You escaped succesfully ')
            return True
        elif player_active_pokemon.get_speed() <= enemy_active_pokemon.get_speed():
            print('You could´nt escape ')
            return False

    def display_actions(self, player_active_pokemon, enemy_active_pokemon, player_team):
        print(
            f'{player_active_pokemon.get_name()} (HP: {player_active_pokemon.get_current_hp()}) '
            f'vs {enemy_active_pokemon.get_name()} (HP: {enemy_active_pokemon.get_current_hp()}) ')
        print('Choose an action: ')
        selection = input('1. Attack , 2. Switch, 3. Bag, 4. Flee ')
        if selection == '1':
            self.attack_selection(player_active_pokemon, enemy_active_pokemon)
        elif selection == '2':
            player_active_pokemon = player_team.switch(player_active_pokemon, player_team)
        elif selection == '3':
            self.bag()
        elif selection == '4':
            self.flee(player_active_pokemon, enemy_active_pokemon)
        return player_active_pokemon

    def attack_enemy(self, player_active_pokemon, enemy_active_pokemon, ability):
        hitroll = player_active_pokemon.hitchance(POKEMON_ATTACK_VALUES[ability]['Accuracy'])
        if "hit" == hitroll:
            damage = player_active_pokemon.get_atk() * (
                        0.01 * (int(POKEMON_ATTACK_VALUES[ability]['Attack_Strength']))) / (
                                 1 + (enemy_active_pokemon.get_defense() / 200))
            damage = int(max(1, damage))
            enemy_active_pokemon.take_damage(damage)
            print(
                f'{player_active_pokemon.get_name()} attacked {enemy_active_pokemon.get_name()} for {damage} damage! ')
            print(f'{enemy_active_pokemon.get_name()} has {enemy_active_pokemon.get_current_hp()} HP left ')
        elif "miss" == hitroll:
            print(f'{player_active_pokemon.get_name()} misses {enemy_active_pokemon.get_name()}')
            pass
        elif "crit" == hitroll:
            damage = (player_active_pokemon.get_atk() * 1.5) * (
                        0.01 * (int(POKEMON_ATTACK_VALUES[ability]['Attack_Strength']))) / (
                                 1 + (enemy_active_pokemon.get_defense() / 200))
            damage = int(max(1, damage))
            enemy_active_pokemon.take_damage(damage)
            print(f'{player_active_pokemon.get_name()} landed a critical hit!')
            print(
                f'{player_active_pokemon.get_name()} attacked {enemy_active_pokemon.get_name()} for {damage} damage! ')
            print(f'{enemy_active_pokemon.get_name()} has {enemy_active_pokemon.get_current_hp()} HP left ')

    def attack_player(self, player_active_pokemon, enemy_active_pokemon):
        ability = enemy_active_pokemon.random_ability()
        print(f'{enemy_active_pokemon.get_name()} uses {ability}')
        hitroll = player_active_pokemon.hitchance(POKEMON_ATTACK_VALUES[ability]['Accuracy'])
        if "hit" == hitroll:
            damage = enemy_active_pokemon.get_atk() * (
                        0.01 * (int(POKEMON_ATTACK_VALUES[ability]['Attack_Strength']))) / (
                                 1 + (player_active_pokemon.get_defense() / 200))
            damage = int(max(1, damage))
            player_active_pokemon.take_damage(damage)
            print(
                f'{enemy_active_pokemon.get_name()} attacked {player_active_pokemon.get_name()} for {damage} damage! ')
            print(f'{player_active_pokemon.get_name()} has {player_active_pokemon.get_current_hp()} HP left ')
        elif "miss" == hitroll:
            print(f'{enemy_active_pokemon.get_name()} misses {player_active_pokemon.get_name()}')
            pass
        elif "crit" == hitroll:
            damage = (enemy_active_pokemon.get_atk() * 1.5) * (
                        0.01 * (int(POKEMON_ATTACK_VALUES[ability]['Attack_Strength']))) / (
                                 1 + (player_active_pokemon.get_defense() / 200))
            damage = int(max(1, damage))
            player_active_pokemon.take_damage(damage)
            print(f'{enemy_active_pokemon.get_name()} landed a critical hit!')
            print(
                f'{enemy_active_pokemon.get_name()} attacked {player_active_pokemon.get_name()} for {damage} damage! ')
            print(f'{player_active_pokemon.get_name()} has {player_active_pokemon.get_current_hp()} HP left ')
