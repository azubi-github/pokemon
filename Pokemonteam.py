import random

from Pokemon import Pokemon
from pokemonlist import POKEMON_DATA


class PokemonTeam:
    def __init__(self):
        self._team = []

    def add_pokemon(self, pokemon):
        self._team.append(pokemon)

    def get_team(self):
        return self._team

    def remove_pokemon(self, index):
        if index is not None and index <= len(self._team):
            removed_pokemon = self._team.pop(index)
            print(f'{removed_pokemon.get_name()} has been removed from the team.')
        else:
            print("Invalid index! No Pokémon removed.")

    def get_index(self, index):
        if 0 <= index < len(self._team):
            return self._team[index]
        return None

    def get_team_names(self):
        team_names = []
        for pokemon in self.get_team():
            team_names.append(pokemon.get_name())
        return team_names

    def switch(self):
        print('Which Pokémon should be sent in? ')
        for i, pokemon in enumerate(self._team):
            print(f"{i + 1}. {pokemon.get_name()}")

        while True:
            try:
                team_number = int(input("Enter the number of the Pokémon: ")) - 1
                if 0 <= team_number < len(self._team):
                    player_active_pokemon = self._team[team_number]
                    print(f'{player_active_pokemon.get_name()} is now active.')
                    return player_active_pokemon
                else:
                    print("Invalid selection! Please choose a valid Pokémon.")
            except ValueError:
                print("Please enter a number.")

    def get_team_len(self):
        return len(self._team)

    def player_team_creation(self):
        player_team_names = []
        print("Build your Team ")
        while True:
            pokemon_name = input("Pokemon name: ").strip().capitalize()
            for line in POKEMON_DATA.keys():
                if pokemon_name in POKEMON_DATA:
                    if pokemon_name == POKEMON_DATA[line]['name']:
                        if pokemon_name in player_team_names:
                            print(f"{pokemon_name} is already in your Team ")
                        else:
                            choice = Pokemon(**POKEMON_DATA[pokemon_name])
                            self.add_pokemon(choice)
                            player_team_names.append(pokemon_name)
                            print(f'{pokemon_name} {choice.get_ability_name_list()} added to your Team ')
                            print(f'Your Team: {player_team_names} ')
                else:
                    print('Pokemon isnt avalible ')
            if self.get_team_len() >= 6:
                break
            else:
                another = input("Another Pokemon? (yes/no) ").lower().strip()
                if another == "yes":
                    pass
                else:
                    if len(player_team_names) <= 0:
                        print("Atleast 1 Pokemon needed ")
                    else:
                        break

    def random_team_creation(self, team_size):
        random_pokemon_list = []
        for x in range(team_size):
            while True:
                random_pokemon = random.choice(list(POKEMON_DATA.keys()))
                if random_pokemon in random_pokemon_list:
                    pass
                else:
                    random_pokemon_list.append(random_pokemon)
                    break
        for line in random_pokemon_list:
            random_choice = Pokemon(**POKEMON_DATA[line])
            self.add_pokemon(random_choice)

    def __repr__(self):
        return str(self._team)

    def __getitem__(self, index):
        return self.get_index(index)
