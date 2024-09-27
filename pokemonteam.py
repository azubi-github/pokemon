class PokemonTeam:
    def __init__(self, player_active_pokemon):
        self.team = []
        self.player_active_pokemon = player_active_pokemon

    def add_pokemon(self, pokemon):
        self.team.append(pokemon)

    def get_team(self):
        return self.team

    def remove_pokemon(self):
        pass

    def __repr__(self):
        return str(self.team)
asd