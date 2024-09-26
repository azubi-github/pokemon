class PokemonTeam:
    def __init__(self):
        self.team = []

    def add_pokemon(self, pokemon):
        self.team.append(pokemon)

    def __repr__(self):
        return str(self.team)
