import pygame
from Battle import Battle
from Pokemon import Pokemon
from pokemonlist import *
from ui_teambuilder import team_builder

def battle_scene():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    DARK_RED = (139, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pokemon Battle Layout")

    enemy_pos = (155, 380)
    player_pos = (550, 125)

    squirtle_img = pygame.image.load("imiges/squirtle.png")
    squirtle_back_img = pygame.image.load("imiges/squirtleback.png")
    charmander_img = pygame.image.load("imiges/charmander.png")
    bulbasaur_img = pygame.image.load("imiges/bulbasaur.png")

    squirtle_img = pygame.transform.scale(squirtle_img, (100, 100))
    charmander_img = pygame.transform.scale(charmander_img, (100, 100))
    bulbasaur_img = pygame.transform.scale(bulbasaur_img, (100, 100))

    squirtle = Pokemon(name=POKEMON_DATA['Squirtle']['name'], element=POKEMON_DATA['Squirtle']['element'],
                       hp=POKEMON_DATA['Squirtle']['health'], dev=POKEMON_DATA['Squirtle']['defense'],
                       spd=POKEMON_DATA['Squirtle']['speed'], atk=POKEMON_DATA['Squirtle']['attack'])
    charmander = Pokemon(name=POKEMON_DATA['Charmander']['name'], element=POKEMON_DATA['Charmander']['element'],
                         hp=POKEMON_DATA['Charmander']['health'], dev=POKEMON_DATA['Charmander']['defense'],
                         spd=POKEMON_DATA['Charmander']['speed'], atk=POKEMON_DATA['Charmander']['attack'])

    HEALTH_BAR_WIDTH = 100
    HEALTH_BAR_HEIGHT = 10

    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 80, 100, 40)

    def draw_health_bar(screen, x, y, health, max_health):
        pygame.draw.rect(screen, RED, (x, y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
        pygame.draw.rect(screen, GREEN, (x, y, (health / max_health) * HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))

    running = True

    battle_instance = Battle(charmander, squirtle, enemy_team=None, player_team=None)

    while running:
        screen.fill('lightblue')

        pygame.draw.ellipse(screen, (139, 69, 19), (100, 400, 200, 100))
        pygame.draw.ellipse(screen, (139, 69, 19), (500, 150, 200, 100))

        screen.blit(squirtle_back_img, enemy_pos)
        screen.blit(charmander_img, player_pos)

        squirtle_health = squirtle.get_current_hp()
        charmander_health = charmander.get_current_hp()

        draw_health_bar(screen, 150, 360, squirtle_health, 100)
        draw_health_bar(screen, 545, 110, charmander_health, 100)

        pygame.draw.rect(screen, RED, button_rect)
        font = pygame.font.Font(None, 30)
        text = font.render("Attack!", True, WHITE)
        screen.blit(text, (button_rect.x + 15, button_rect.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    battle_instance.attack_selection(squirtle, charmander)

        pygame.display.update()

    # Quit Pygame
    pygame.quit()


def gui():
    team_builder()
    #battle_scene()


gui()
