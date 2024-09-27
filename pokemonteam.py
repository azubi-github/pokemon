class PokemonTeam:
    def __init__(self):
        self.team = []

    def add_pokemon(self, pokemon):
        self.team.append(pokemon)

    def get_team(self):
        return self.team

    def get_team_len(self):
        return len(self.team)

    def remove_pokemon(self):
        pass

    def __repr__(self):
        return str(self.team)
