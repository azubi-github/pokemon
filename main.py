import interface
from Pokemon import Pokemon
from pokemonlist import POKEMON_DATA
from Pokemonteam import PokemonTeam
import random
from Battle import Battle
from interface import gui


def start_gui():
    gui()


player_team = PokemonTeam()
player_team_names = []
enemy_team = PokemonTeam()
enemy_team_names = []
random_pokemon = []
player_choosing = True
turn = 0
skip_turn = False

print("Build your Team ")
while player_choosing:
    pokemon_name = input("Pokemon name: ").strip().capitalize()

    for line in POKEMON_DATA.keys():
        if pokemon_name in POKEMON_DATA:
            if pokemon_name == POKEMON_DATA[line]['name']:
                if pokemon_name in player_team_names:
                    print(f"{pokemon_name} is already in your Team ")
                    break
                else:
                    choice = Pokemon(name=POKEMON_DATA[pokemon_name]['name'],
                                     element=POKEMON_DATA[pokemon_name]['element'],
                                     hp=POKEMON_DATA[pokemon_name]['health'],
                                     dev=POKEMON_DATA[pokemon_name]['defense'],
                                     spd=POKEMON_DATA[pokemon_name]['speed'],
                                     atk=POKEMON_DATA[pokemon_name]['attack'])
                    player_team.add_pokemon(choice)
                    player_team_names.append(pokemon_name)
                    print(f'{pokemon_name} {choice.get_ability_list()} added to your Team ')
                    print(f'Your Team: {player_team_names} ')
                    break
        else:
            print('Pokemon isnt avalible ')
            break
    if len(player_team_names) >= 6:
        player_choosing = False
    else:
        another = input("Another Pokemon? (yes/no) ").lower().strip()
        if another == "yes":
            player_choosing = True
        else:
            if len(player_team_names) <= 0:
                print("Atleast 1 Pokemon needed ")
                player_choosing = True
            else:
                break

enemy_team_number = len(player_team_names)
for x in range(enemy_team_number):
    temphold = random.choice(list(POKEMON_DATA.keys()))
    random_pokemon.append(temphold)

for line in random_pokemon:
    random_choice = Pokemon(name=POKEMON_DATA[line]['name'],
                            element=POKEMON_DATA[line]['element'],
                            hp=POKEMON_DATA[line]['health'],
                            dev=POKEMON_DATA[line]['defense'],
                            spd=POKEMON_DATA[line]['speed'],
                            atk=POKEMON_DATA[line]['attack'])
    enemy_team.add_pokemon(random_choice)
    enemy_team_names.append(POKEMON_DATA[line]['name'])

choose_fight = str(input('Do you want an Interface? (y/n) ').lower().strip())

if choose_fight == 'n':
    if len(player_team_names) > 1:
        print('Which Pokémon should be sent in first? ')
        for i, pokemon in enumerate(player_team_names):
            print(f"{i + 1}. {pokemon}")
        while True:
            try:
                team_number = int(input("Enter the number of the Pokémon: ")) - 1
                if 0 <= team_number < len(player_team_names):
                    player_active_pokemon = player_team[team_number]
                    break
                else:
                    print('Invalid selection ')
            except ValueError:
                print('Please enter a number ')
    else:
        player_active_pokemon = player_team[0]
    enemy_active_pokemon = random.choice(enemy_team.get_team())

    battle_instance = Battle(enemy_active_pokemon, player_active_pokemon, enemy_team, player_team, enemy_team_number)
    battle_instance.start_battle(enemy_active_pokemon, player_active_pokemon)
    fighting = True
if choose_fight == 'y':
    gui()

while fighting:
    if turn % 2 == 1 and turn <= 3:
        turn += 1
        if skip_turn != True:
            player_active_pokemon = battle_instance.display_actions(player_active_pokemon, enemy_active_pokemon, player_team)
        enemy_active_pokemon, skip_turn = battle_instance.check_enemy_fainted(enemy_active_pokemon, enemy_team)
        if enemy_team.get_team_len() <= 0:
            print(f'Your team {player_team_names} won the fight!')
            fighting = False
            break
    elif turn % 2 == 0 and turn != 0 and turn <= 2:
        turn += 1
        if skip_turn != True:
            battle_instance.enemy_turn(player_active_pokemon, enemy_active_pokemon)
        player_active_pokemon, skip_turn = battle_instance.check_player_fainted(player_active_pokemon, player_team)
        if player_team.get_team_len() <= 0:
            print(f'The enemy team {enemy_team_names} won the fight..')
            fighting = False
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