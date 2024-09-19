
class Battle:
    def __init__(self, enemy_active_pokemon, player_active_pokemon):
        self.enemy_pokemon = enemy_active_pokemon
        self.player_pokemon = player_active_pokemon

    def roll_speed(self):
        if self.player_pokemon.team[0].get_speed() > self.enemy_pokemon.team[0].get_speed():
            print(f'{self.player_pokemon} is faster ')
        else:
            print(f'{self.enemy_pokemon} is faster ')

    def start_battle(self, enemy_active_pokemon, player_active_pokemon):
        print(f'Enemy Pokemon: {enemy_active_pokemon}')
        print(f'Player Pokemon: {player_active_pokemon}')
        self.roll_speed()

    def display_actions(self, player_pokemon, enemy_pokemon):
        print(
            f'{player_pokemon.get_name()} (HP: {player_pokemon.get_hp()}) vs {enemy_pokemon.get_name()} (HP: {enemy_pokemon.get_hp()})')
        print('Choose an action: ')
        print('1. Attack')
        print('2. Switch')
        print('3. Bag ')
        print('4. Flee')
