import pygame
from Pokemonteam import PokemonTeam
from pokemonlist import *
from Pokemon import Pokemon


def team_builder():
    pygame.init()

    screen_width = 800
    screen_height = 600
    color_white = (255, 255, 255)
    color_green = (0, 255, 0)
    color_black = (0, 0, 0)

    team_builder_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Pokémon Team Builder ')

    player_team = PokemonTeam()
    running = True

    scroll_position = 0
    total_pokemon_height = len(POKEMON_DATA) * 30
    max_scroll = max(total_pokemon_height - screen_height + 50, 0)

    def draw_team():
        font = pygame.font.Font(None, 30)
        team_header = font.render('Team List: ', True, color_black)
        team_builder_screen.blit(team_header, (300, 20))
        for i, pokemon in enumerate(player_team.get_team()):
            display_text = f'{pokemon.get_name()} [{pokemon.get_element()}]'
            text = font.render(display_text, True, color_green)
            team_builder_screen.blit(text, (300, 50 + i * 30))

    while running:
        team_builder_screen.fill(color_white)

        font = pygame.font.Font(None, 30)
        selection_header = font.render('Pokemon List: ', True, color_black)
        team_builder_screen.blit(selection_header, (30, 20))

        for i, (name, data) in enumerate(POKEMON_DATA.items()):
            display_text = f'{name} [{data['element']}]'
            text = font.render(display_text, True, color_black)
            text_rect = text.get_rect(topleft=(30, 50 + scroll_position + i * 30))
            team_builder_screen.blit(text, text_rect)

            if text_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                choice = Pokemon(**data)
                if player_team.get_team_len() < 6:
                    if choice not in player_team.get_team():
                        player_team.add_pokemon(choice)
                else:
                    print('Team is full ')

        draw_team()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEWHEEL:
                scroll_position += event.y * 30
                scroll_position = max(min(scroll_position, max_scroll), 0)
        pygame.display.update()

    pygame.quit()

team_builder()
