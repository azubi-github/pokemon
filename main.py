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

print(enemy_team_names)
ask_fight = input("Start a fight? (yes/no) ").strip().lower()

if ask_fight == "yes":
    current_enemy_pokemon = enemy_team.team[0]
    if len(player_team_names) > 1:
        first_pokemon = input(f'{player_team_names} which Pokemon should go first? (1-3) ').strip()
        if first_pokemon == '1':
            current_player_pokemon = player_team.team[0]
        elif first_pokemon == '2':
            current_player_pokemon = player_team.team[1]
        elif first_pokemon == '3':
            current_player_pokemon = player_team.team[2]
        else:
            print('Team slot is empty!')
    else:
        current_player_pokemon = player_team.team[0]
    print(f'{current_player_pokemon.get_name()} is you current pokemon')
    print("TO BATTLE! ")
    battle_instance = Battle(enemy_team, player_team)
    battle_instance.start_battle(current_enemy_pokemon, current_player_pokemon)
    fighting = True

else:
    print("Bye ")
    fighting = False


while fighting:
    battle_instance.display_actions(current_player_pokemon, current_enemy_pokemon)
    if current_enemy_pokemon.get_current_hp() <= 0:
        print(f'{current_enemy_pokemon.get_name()} fainted... ')
    battle_instance.attack_player(current_player_pokemon, current_enemy_pokemon)
    if current_player_pokemon.get_current_hp() <= 0:
        print(f'{current_player_pokemon.get_name()} fainted... ')
        battle_instance.switch()





