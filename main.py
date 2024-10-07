from Pokemon import Pokemon
from pokemonlist import POKEMON_DATA
from Pokemonteam import PokemonTeam
import random
from Battle import Battle

player_team = []
player_team_names = []
enemy_team = []
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
                                     hp=POKEMON_DATA[pokemon_name]['health'],
                                     dev=POKEMON_DATA[pokemon_name]['defense'],
                                     spd=POKEMON_DATA[pokemon_name]['speed'],
                                     atk=POKEMON_DATA[pokemon_name]['attack'])
                    player_team.append(choice)
                    player_team_names.append(pokemon_name)
                    print(f'{pokemon_name} {choice.get_ability_list()} added to your Team ')
                    print(f'Your Team: {player_team_names} ')
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

for line in random_pokemon:
    random_choice = Pokemon(name=POKEMON_DATA[line]['name'],
                            element=POKEMON_DATA[line]['element'],
                            hp=POKEMON_DATA[line]['health'],
                            dev=POKEMON_DATA[line]['defense'],
                            spd=POKEMON_DATA[line]['speed'],
                            atk=POKEMON_DATA[line]['attack'])
    enemy_team.append(random_choice)
    enemy_team_names.append(POKEMON_DATA[line]['name'])

current_enemy_pokemon = enemy_team[0]

if len(player_team_names) > 1:
    while True:
        first_pokemon = int(input(f'{player_team_names} which Pokemon should go first? (1-{len(player_team_names)}) ').strip())
        if first_pokemon < 1 or first_pokemon > len(player_team_names):
            print('Team slot is empty! ')
            continue
        else:
            current_player_pokemon = player_team[first_pokemon - 1]
            break
else:
    current_player_pokemon = player_team[0]

print(f'{current_player_pokemon.get_name()} is you current pokemon ')
battle_instance = Battle(enemy_team, player_team)
battle_instance.start_battle(current_enemy_pokemon, current_player_pokemon)
fighting = True

while fighting:
    battle_instance.display_actions(current_player_pokemon, current_enemy_pokemon, player_team)
    if battle_instance.check_fainted(current_player_pokemon, current_enemy_pokemon):
        fighting = False
        break
    battle_instance.enemy_turn(current_player_pokemon, current_enemy_pokemon)
    if battle_instance.check_fainted(current_player_pokemon, current_enemy_pokemon):
        fighting = False
        break


