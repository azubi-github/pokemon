import pygame
from pokemon import Pokemon
from pokemonlist import POKEMON_DATA, POKEMON_ATTACK
from pokemonteam import PokemonTeam
import random
from battle import Battle

player_team = PokemonTeam()
player_team_names = []
enemy_team = PokemonTeam()
enemy_team_names = []
random_pokemon = []
player_choosing = True

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
                                     hp=POKEMON_DATA[pokemon_name]['health'], dev=POKEMON_DATA[pokemon_name]['defense'],
                                     spd=POKEMON_DATA[pokemon_name]['speed'], ability=POKEMON_ATTACK['Ember'],
                                     atk=POKEMON_DATA[pokemon_name]['attack'])
                    player_team.add_pokemon(choice)
                    player_team_names.append(pokemon_name)
                    print(f'{pokemon_name} added to your Team ')
                    print(player_team_names)
                    break
        else:
            print('Pokemon isnt avalible ')
            break
    if len(player_team_names) == 3:
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

pokemon_list = []
for line in random_pokemon:
    random_choice = Pokemon(name=POKEMON_DATA[line]['name'], element=POKEMON_DATA[line]['element'],
                            hp=POKEMON_DATA[line]['health'], dev=POKEMON_DATA[line]['defense'],
                            spd=POKEMON_DATA[line]['speed'], ability=POKEMON_ATTACK['Vine_Whip'],
                            atk=POKEMON_DATA[line]['attack'])
    enemy_team.add_pokemon(random_choice)
    enemy_team_names.append(POKEMON_DATA[line]['name'])

print(player_team)
print(enemy_team)
ask_fight = input("Start a fight? (yes/no) ").strip().lower()

if ask_fight == "yes":
    print("TO BATTLE! ")
    battle_instance = Battle(enemy_team, player_team)
    battle_instance.start_battle(enemy_team.team[0], player_team.team[0])
    fighting = True

else:
    print("Bye ")
    fighting = False


while fighting:
    battle_instance.roll_speed()
    battle_instance.display_actions(player_team.team[0], enemy_team.team[0])
    if battle_instance.check_fainted(player_team.team[0], enemy_team.team[0]):
        fighting = False
        break
    battle_instance.enemy_turn(player_team.team[0], player_team.team[0])
    if battle_instance.check_fainted(player_team.team[0], enemy_team.team[0]):
        fighting = False
        break








