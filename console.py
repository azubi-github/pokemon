from Pokemonteam import PokemonTeam
import random
from Battle import Battle

player_team = PokemonTeam()
enemy_team = PokemonTeam()

random_team_choice = input("Do you want to create your own Team?\nIf no then it will be randomly created yes/no \n")
if random_team_choice == "yes":
    player_team.player_team_creation()
else:
    while True:
        random_team_size = int(input("How big do you want your Team? 1-6 \n"))
        if 6 > random_team_size > 0:
            break
        else:
            print("Error, please use a Number between 1-6")
    player_team.random_team_creation(random_team_size)
enemy_team_number = player_team.get_team_len()
enemy_team.random_team_creation(enemy_team_number)

player_team_names = player_team.get_team_name()
enemy_team_names = enemy_team.get_team_name()


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
battle_instance.fight(player_active_pokemon, enemy_active_pokemon, player_team, enemy_team, enemy_team_names, player_team_names)