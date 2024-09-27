class PokemonTeam:
    def __init__(self, player_active_pokemon):
        self.team = []
        self.player_active_pokemon = self.team[0]

    def add_pokemon(self, pokemon):
        self.team.append(pokemon)

    def get_team(self):
        return self.team

    def remove_pokemon(self):
        pass

    def switch(self, player_pokemon_team, player_active_pokemon):
        print('Which Pokemon should be send in? ')
        team_number = int(input(f'{player_pokemon_team} )'))
        player_active_pokemon = player_pokemon_team[team_number - 1]
        print(player_active_pokemon)

    def __repr__(self):
        return str(self.team)
