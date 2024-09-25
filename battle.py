
class Battle:
    def __init__(self, enemy_active_pokemon, player_active_pokemon):
        self.enemy_pokemon = enemy_active_pokemon
        self.player_pokemon = player_active_pokemon

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
        attack = input('choose your attack: Ember, Vine Whip, Water Gun (1-3) ')
        if attack == '1':
            self.attack_enemy(player_active_pokemon, enemy_active_pokemon)
        elif attack == '2':
            self.attack_enemy(player_active_pokemon, enemy_active_pokemon)
        elif attack == '3':
            self.attack_enemy(player_active_pokemon, enemy_active_pokemon)
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
            f'{player_active_pokemon.get_name()} (HP: {player_active_pokemon.get_current_hp()}) '
            f'vs {enemy_active_pokemon.get_name()} (HP: {enemy_active_pokemon.get_current_hp()})')
        print('Choose an action: ')
        selection = input('1. Attack , 2. Switch, 3. Bag, 4. Flee ')
        if selection == '1':
            self.attack_selection(player_active_pokemon, enemy_active_pokemon)
        elif selection == '2':
            self.switch()
        elif selection == '3':
            self.bag()
        elif selection == '4':
            self.flee(player_active_pokemon, enemy_active_pokemon)

    def attack_enemy(self, player_active_pokemon, enemy_active_pokemon):
        damage = player_active_pokemon.get_atk() - enemy_active_pokemon.get_defense()
        damage = int(max(1, damage))
        enemy_active_pokemon.take_damage(damage)
        print(f'{player_active_pokemon.get_name()} attacked {enemy_active_pokemon.get_name()} for {damage} damage! ')
        print(f'{enemy_active_pokemon.get_name()} has {enemy_active_pokemon.get_current_hp()} HP left ')

    def attack_player(self, player_active_pokemon, enemy_active_pokemon):
        damage = enemy_active_pokemon.get_atk() - player_active_pokemon.get_defense()
        damage = int(max(1, damage))
        player_active_pokemon.take_damage(damage)
        print(f'{enemy_active_pokemon.get_name()} attacked {player_active_pokemon.get_name()} for {damage} damage! ')
        print(f'{player_active_pokemon.get_name()} has {player_active_pokemon.get_current_hp()} HP left ')
