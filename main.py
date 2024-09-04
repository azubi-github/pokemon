from pokemon import Pokemon
from pokemonteam import PokemonTeam
import random

player_team = PokemonTeam()
enemy_team = PokemonTeam()
yes_counter = 1

print("Build your Team")

player_choosing = True

while player_choosing:
    pokemon_name = input("Pokemon name: ")
    with open("C:\\Users\\lukas_langer\\Desktop\\PycharmProjects\\Pokemon\\pokemonlist.txt", "r") as file:
        pokemon_file = file.readlines()

    for line in pokemon_file:
        pokemon_list = line.strip().split(",")

        if pokemon_name.lower() == pokemon_list[0]:
            choice = Pokemon(pokemon_list[0], pokemon_list[1], pokemon_list[2], pokemon_list[3], pokemon_list[4],
                             pokemon_list[5], pokemon_list[6])
            player_team.add_pokemon(choice)
            print(f'{pokemon_name} added to the Team')
            break
    another = input("Another Pokemon? (yes/no)").lower().strip()

    if another == "yes":
        yes_counter += 1

    elif another != "yes":
        player_choosing = False

with open("C:\\Users\\lukas_langer\\Desktop\\PycharmProjects\\Pokemon\\pokemonlist.txt", "r") as file:
    pokemon_file = file.readlines()

enemy_team_number = yes_counter
random_pokemon = random.sample(pokemon_file, enemy_team_number)

for line in random_pokemon:
    pokemon_list = line.strip().split(",")
    choice = Pokemon(pokemon_list[0], pokemon_list[1], pokemon_list[2], pokemon_list[3], pokemon_list[4],
                     pokemon_list[5], pokemon_list[6])
    enemy_team.add_pokemon(choice)

print("Your Team")
list()

ask_fight = input("Start a fight? (yes/no)").strip().lower()
if ask_fight == "yes":
    print("TO BATTLE!")
    fighting = True
else:
    print(":(")







