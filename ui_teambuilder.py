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
    pygame.display.set_caption('Pokémon Team Builder')

    player_team = PokemonTeam()
    added_pokemon = player_team.get_team_names()
    running = True

    clicked_pokemon_index = None
    scroll_position = 0

    def draw_team():
        font = pygame.font.Font(None, 30)
        team_header = font.render('Team List:', True, color_black)
        team_builder_screen.blit(team_header, (300, 20))
        for i, pokemon in enumerate(player_team.get_team()):
            display_text = f'{i + 1}. {pokemon.get_name()} [{pokemon.get_element()}]'
            text_color = color_green
            text = font.render(display_text, True, text_color)
            team_builder_screen.blit(text, (300, 50 + i * 30))

            if text.get_rect(topleft=(300, 50 + i * 30)).collidepoint(pygame.mouse.get_pos()) and \
                    pygame.mouse.get_pressed()[0]:
                player_team.remove_pokemon(i)
                added_pokemon.remove(pokemon.get_name())

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        team_builder_screen.fill(color_white)

        font = pygame.font.Font(None, 30)
        selection_header = font.render('Pokemon List:', True, color_black)
        team_builder_screen.blit(selection_header, (30, 20 + scroll_position))

        for i, (name, data) in enumerate(POKEMON_DATA.items()):
            display_text = f'{name} [{data["element"]}]'

            text_color = color_green if name in added_pokemon else color_black
            text = font.render(display_text, True, text_color)
            text_rect = text.get_rect(topleft=(30, 50 + scroll_position + i * 30))
            team_builder_screen.blit(text, text_rect)

            if text.get_rect(topleft=(30, 50 + i * 30)).collidepoint(pygame.mouse.get_pos()) and \
                    pygame.mouse.get_pressed()[0]:
                choice = Pokemon(**data)
                if name not in added_pokemon and player_team.get_team_len() < 6:
                    player_team.add_pokemon(choice)
                    added_pokemon.append(name)

        draw_team()
        pygame.display.flip()

    pygame.quit()


team_builder()
