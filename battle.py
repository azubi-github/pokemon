
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

    def check_fainted(self, player_active_pokemon, enemy_active_pokemon):
        if player_active_pokemon.get_current_hp() <= 0:
            print('Your Pokemon fainted.. ')
            return True
        elif enemy_active_pokemon.get_current_hp() <= 0:
            print('Enemy Pokemon fainted!! ')
            return True

    def attack_selection(self, player_active_pokemon, enemy_active_pokemon):
        print('choose your attack: Ember, Vine Whip, Water Gun (1-3) ')
        attack = input()
        if attack == '1':
            player_active_pokemon.attack_enemy(enemy_active_pokemon, player_active_pokemon)
        elif attack == '2':
            player_active_pokemon.attack_enemy(enemy_active_pokemon, player_active_pokemon)
        elif attack == '3':
            player_active_pokemon.attack_enemy(enemy_active_pokemon, player_active_pokemon)
        else:
            print('Choose between 1-3 ! ')

    def enemy_turn(self, player_active_pokemon, enemy_active_pokemon):
        enemy_active_pokemon.attack_player(player_active_pokemon, enemy_active_pokemon)

    def bag(self):
        pass

    def switch(self):
        pass

    def flee(self, player_active_pokemon, enemy_active_pokemon):
        if player_active_pokemon.get_speed() >= enemy_active_pokemon.get_speed():
            print('You escaped succesfully ')
            return False
        elif player_active_pokemon.get_speed() <= enemy_active_pokemon.get_speed():
            print('You could´nt escape ')

    def display_actions(self, player_active_pokemon, enemy_active_pokemon):
        print(
            f'{player_active_pokemon.get_name()} (HP: {player_active_pokemon.get_current_hp()}) vs {enemy_active_pokemon.get_name()} (HP: {enemy_active_pokemon.get_current_hp()})')
        print('Choose an action: ')
        print('1. Attack , 2. Switch, 3. Bag, 4. Flee ')
        selection = input()
        if selection == '1':
            self.attack_selection(player_active_pokemon, enemy_active_pokemon)
        elif selection == '2':
            self.switch()
        elif selection == '3':
            self.bag()
        elif selection == '4':
            self.flee(player_active_pokemon, enemy_active_pokemon)


