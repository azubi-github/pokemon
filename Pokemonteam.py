class PokemonTeam:
    def __init__(self):
        self._team = []

    def add_pokemon(self, pokemon):
        self._team.append(pokemon)

    def get_team(self):
        return self._team

    def remove_fainted_pokemon(self, index):
        if 0 <= index <= len(self._team):
            removed_pokemon = self._team.pop(index)
            print(f'{removed_pokemon.get_name()} has been removed from the team.')
        else:
            print("Invalid index! No Pokémon removed.")

    def get_pokemon(self, index):
        if 0 <= index < len(self._team):
            return self._team[index]
        return None

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

    def __repr__(self):
        return str(self._team)

    def __getitem__(self, index):
        return self.get_pokemon(index)
