import random
from math import floor


from pokemonlist import POKEMON_ATTACK_VALUES
from universalfunctions import tryVar


class Battle:

    def __init__(self, enemy_active_pokemon, player_active_pokemon, enemy_team, player_team, team_number):
        self.enemy_pokemon = enemy_active_pokemon
        self.player_pokemon = player_active_pokemon
        self.enemy_team = enemy_team
        self.player_team = player_team
        self.hp_pot = floor(1+(team_number/2))

# Battle erstellen

    def start_battle(self, enemy_active_pokemon, player_active_pokemon):
        print(f'Enemy Pokemon: {enemy_active_pokemon.get_name()} ')
        print(f'Player Pokemon: {player_active_pokemon.get_name()} ')

# Player funktion

    def display_actions(self, player_active_pokemon, enemy_active_pokemon, player_team):
        print(
            f'{player_active_pokemon.get_name()} (HP: {player_active_pokemon.get_current_hp()}) '
            f'vs {enemy_active_pokemon.get_name()} (HP: {enemy_active_pokemon.get_current_hp()}) ')
        print('Choose an action: ')
        selection = input('1. Attack , 2. Switch, 3. Bag, 4. Flee ')
        if selection == '1':
            self.attack_selection(player_active_pokemon, enemy_active_pokemon)
        elif selection == '2':
            player_active_pokemon = player_team.switch()
        elif selection == '3':
            self.bag(player_active_pokemon)
        elif selection == '4':
            self.flee(player_active_pokemon, enemy_active_pokemon)
        return player_active_pokemon

    def attack_selection(self, player_active_pokemon, enemy_active_pokemon):
        abilities = player_active_pokemon.get_ability_list()
        print('Choose an Ability: ')
        for i, ability in enumerate(abilities):
            print(f'{i + 1}. {ability.get_name()}')

        while True:
            try:
                choice = int(input()) - 1
                if choice < 0 or choice > len(abilities):
                    print('Invalid selection ')
                else:
                    ability = player_active_pokemon.get_ability_list()[choice]
                    print(f'{player_active_pokemon.get_name()} uses {ability.get_name()}')
                    self.attack_enemy(player_active_pokemon, enemy_active_pokemon, ability)
                    break
            except ValueError:
                print('Please enter a number ')


    def attack_enemy(self, player_active_pokemon, enemy_active_pokemon, ability):
        hitroll = player_active_pokemon.hitchance(ability.get_accuracy())
        if "hit" == hitroll:
            damage = player_active_pokemon.get_atk() * (
                    0.01 * ability.get_attack_strength()) / (
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
                    0.01 * ability.get_attack_strength()) / (
                             1 + (enemy_active_pokemon.get_defense() / 200))
            damage = int(max(1, damage))
            enemy_active_pokemon.take_damage(damage)
            print(f'{player_active_pokemon.get_name()} landed a critical hit!')
            print(
                f'{player_active_pokemon.get_name()} attacked {enemy_active_pokemon.get_name()} for {damage} damage! ')
            print(f'{enemy_active_pokemon.get_name()} has {enemy_active_pokemon.get_current_hp()} HP left ')

    def bag(self, player_active_pokemon):
        choice = input("What would you like to Choose? \n 1. Health Pot \n 2. TDB \n ")
        print(f"you got {self.hp_pot} pots left!")
        if choice == "1":
            if self.hp_pot > 0:
                player_active_pokemon.healing(50)
                self.hp_pot += -1
                print(self.hp_pot)
        else:
            print("Your out of Health Pots!")

    def flee(self, player_active_pokemon, enemy_active_pokemon):
        if player_active_pokemon.get_speed() > enemy_active_pokemon.get_speed():
            print('You escaped succesfully ')
            return True
        elif player_active_pokemon.get_speed() < enemy_active_pokemon.get_speed():
            print('You could´nt escape ')
            return False
        elif player_active_pokemon.get_speed() == enemy_active_pokemon.get_speed():
            #if random.randint(1, 50)
            pass

    def check_player_fainted(self, player_active_pokemon, player_team):
        team_len = player_team.get_team_len()
        if player_active_pokemon.is_fainted():
            print(f'Your {player_active_pokemon.get_name()} fainted.. ')
            index = player_team.get_team().index(player_active_pokemon)
            player_team.remove_fainted_pokemon(index)
            team_len = team_len - 1
            if team_len >= 1:
                player_active_pokemon = player_team.switch()
            else:
                print('Your team lost..')
                pass
        return player_active_pokemon

# Enemy funktion

    def enemy_turn(self, player_active_pokemon, enemy_active_pokemon):
        self.attack_player(player_active_pokemon, enemy_active_pokemon)

    def attack_player(self, player_active_pokemon, enemy_active_pokemon):
        ability = enemy_active_pokemon.random_ability()
        print(f'{enemy_active_pokemon.get_name()} uses {ability.get_name()}')
        hitroll = player_active_pokemon.hitchance(ability.get_accuracy())
        if "hit" == hitroll:
            damage = enemy_active_pokemon.get_atk() * (
                    0.01 * ability.get_attack_strength()) / (
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
                    0.01 * ability.get_attack_strength()) / (
                             1 + (player_active_pokemon.get_defense() / 200))
            damage = int(max(1, damage))
            player_active_pokemon.take_damage(damage)
            print(f'{enemy_active_pokemon.get_name()} landed a critical hit!')
            print(
                f'{enemy_active_pokemon.get_name()} attacked {player_active_pokemon.get_name()} for {damage} damage! ')
            print(f'{player_active_pokemon.get_name()} has {player_active_pokemon.get_current_hp()} HP left ')

    def check_enemy_fainted(self, enemy_active_pokemon, enemy_team):
        team_len = enemy_team.get_team_len()
        if enemy_active_pokemon.is_fainted():
            print(f'{enemy_active_pokemon.get_name()} fainted.. ')
            index = enemy_team.get_team().index(enemy_active_pokemon)
            enemy_team.remove_fainted_pokemon(index)
            team_len = team_len - 1
            if team_len > 1:
                enemy_active_pokemon = random.choice(enemy_team.get_team())
            elif team_len == 1:
                enemy_active_pokemon = random.choice(enemy_team.get_team())
            elif team_len <= 0:
                pass
        return enemy_active_pokemon

    def fight(self, player_active_pokemon, enemy_active_pokemon, player_team, enemy_team, enemy_team_names, player_team_names):
        turn = 0
        while True:
            if turn % 2 == 1 and turn <= 3:
                turn += 1
                player_active_pokemon = self.display_actions(player_active_pokemon, enemy_active_pokemon,
                                                                        player_team)
                enemy_active_pokemon = self.check_enemy_fainted(enemy_active_pokemon, enemy_team)
                if enemy_team.get_team_len() <= 0:
                    print(f'Your team {player_team_names} won the fight!')
                    break
            elif turn % 2 == 0 and turn != 0 and turn <= 2:
                turn += 1
                self.enemy_turn(player_active_pokemon, enemy_active_pokemon)
                player_active_pokemon = self.check_player_fainted(player_active_pokemon, player_team)
                if player_team.get_team_len() <= 0:
                    print(f'The enemy team {enemy_team_names} won the fight..')
                    break
            elif turn == 0 or turn >= 3:
                turn = 0
                player_speed = player_active_pokemon.get_speed()
                enemy_speed = enemy_active_pokemon.get_speed()
                if player_speed < enemy_speed:
                    turn += 2
                elif player_speed > enemy_speed:
                    turn += 1
                else:
                    turn += random.randint(1, 3)

