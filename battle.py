
class Battle:
    def __init__(self, enemy_active_pokemon, player_active_pokemon):
        self.enemy_pokemon = enemy_active_pokemon
        self.player_pokemon = player_active_pokemon

    def roll_speed(self):
        if self.player_pokemon.team[0].get_speed() > self.enemy_pokemon.team[0].get_speed():
            print(f'{self.player_pokemon} is faster ')
            first_pokemon = self.player_pokemon
            second_pokemon = self.enemy_pokemon

        else:
            print(f'{self.enemy_pokemon} is faster ')
            first_pokemon = self.enemy_pokemon
            second_pokemon = self.player_pokemon

    def start_battle(self, enemy_active_pokemon, player_active_pokemon):
        print(f'Enemy Pokemon: {enemy_active_pokemon}')
        print(f'Player Pokemon: {player_active_pokemon}')
        self.roll_speed()

    def attack_selection(self):
        print('choose your attack: Ember, Vine Whip, Water Gun (1-3) ')
        attack = input()
        if attack == '1':
            self.player_pokemon.
        if attack == '2':

        if attack == '3':

    def bag(self):
        pass

    def switch(self):
        pass

    def flee(self):
        if self.player_pokemon.get_speed() >= self.enemy_pokemon.get_speed():
            print('You escaped succesfully ')
        elif self.player_pokemon.get_speed() <= self.enemy_pokemon.get_speed():
            print('You could´nt escape ')

    def display_actions(self, player_pokemon, enemy_pokemon):
        print(
            f'{player_pokemon.get_name()} (HP: {player_pokemon.get_current_hp()}) vs {enemy_pokemon.get_name()} (HP: {enemy_pokemon.get_current_hp()})')
        print('Choose an action: ')
        print('1. Attack , 2. Switch, 3. Bag, 4. Flee ')
        selection = input()
        if selection == '1':
            self.attack_selection()
        elif selection == '2':
            pass
        elif selection == '3':
            pass
        elif selection == '4':
            self.flee()


