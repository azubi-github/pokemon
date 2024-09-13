import pygame
from pokemon import Pokemon
from pokemonlist import POKEMON_DATA, POKEMON_ATTACK
from pokemonteam import PokemonTeam
import random

player_team = PokemonTeam()
player_team_names = []
enemy_team = PokemonTeam()
enemy_team_names = []

player_choosing = True

#with open("C:\\Users\\lukas_langer\\Desktop\\PycharmProjects\\Pokemon\\pokemonlist.txt", "r") as file:
 #   pokemon_file = file.readlines()

print("Build your Team ")

while player_choosing:
    pokemon_name = input("Pokemon name: ").strip().capitalize()

    pokemon_found = False

    for line in POKEMON_DATA.keys():

        if pokemon_name == POKEMON_DATA[line]['name']:

            if pokemon_name in player_team_names:
                print(f"{pokemon_name} is already in your Team ")
                break

            else:

                choice = Pokemon(name=POKEMON_DATA[pokemon_name]['name'],element=POKEMON_DATA[pokemon_name]['element'],
                                 hp=POKEMON_DATA[pokemon_name]['health'],dev=POKEMON_DATA[pokemon_name]['defense'],
                                 spd=POKEMON_DATA[pokemon_name]['speed'],ability=POKEMON_ATTACK['Vine_Whip'],
                                 atk=POKEMON_DATA[pokemon_name]['attack'])
                print(choice)
                player_team.add_pokemon(choice)
                player_team_names.append(POKEMON_DATA[pokemon_name])
                print(f'{pokemon_name} added to your Team ')
            pokemon_found = True
            break

    another = input("Another Pokemon? (yes/no) ").lower().strip()

    if another != "yes":
        player_choosing = False

enemy_team_number = len(player_team_names)
#funkt noch net
print(enemy_team_number)
random_pokemon = []
#funkt noch net
for x in range(enemy_team_number):
    temphold = random.choice(list(POKEMON_DATA.items()))
    print(temphold)
    random_pokemon.append(temphold)
print(random_pokemon)
for line in random_pokemon:
    pokemon_list = line.strip().split(",")
    choice = Pokemon(*pokemon_list)
    enemy_team.add_pokemon(choice)
    enemy_team_names.append(pokemon_list[0])

print(player_team)

ask_fight = input("Start a fight? (yes/no) ").strip().lower()

if ask_fight == "yes":
    print("TO BATTLE! ")
    fighting = True

else:
    print("Bye ")


while fighting:
    pass



