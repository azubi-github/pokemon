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
    #team_builder_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Pokémon Team Builder ')

    player_team = PokemonTeam()
    added_pokemon = {pokemon.get_name() for pokemon in player_team.get_team()}
    running = True

    clicked_pokemon_index = None
    scroll_position = 0

    def draw_team():
        font = pygame.font.Font(None, 30)
        team_header = font.render('Team List: ', True, color_black)
        team_builder_screen.blit(team_header, (300, 20))
        for i, pokemon in enumerate(player_team.get_team()):
            number = i + 1
            display_text = f'{number}. {pokemon.get_name()} [{pokemon.get_element()}]'
            text = font.render(display_text, True, color_green)
            team_builder_screen.blit(text, (300, 50 + i * 30))

            text = font.render(display_text, True, color_black)
            text_rect = text.get_rect(topleft=(300, 50 + i * 30))
            team_builder_screen.blit(text, text_rect)

            if text_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                removed_pokemon = Pokemon.get_pokemon()
                print(f'{Pokemon.get_pokemon()}')
                #choice = player_team.get_index()
                #remove_pokemon()

    def remove_pokemon():
        index = player_team.get_team().index(Pokemon)
        player_team.remove_pokemon(index)

    def add_pokemon():
        pass

    def display_pokemon():
        pass

    while running:
        team_builder_screen.fill(color_white)

        font = pygame.font.Font(None, 30)
        selection_header = font.render('Pokemon List: ', True, color_black)
        team_builder_screen.blit(selection_header, (30, 20 + scroll_position))

        for i, (name, data) in enumerate(POKEMON_DATA.items()):
            display_text = f'{name} [{data['element']}]'

            if name in added_pokemon:
                text_color = color_green
            else:
                text_color = color_black

            text = font.render(display_text, True, text_color)
            text_rect = text.get_rect(topleft=(30, 50 + scroll_position + i * 30))
            team_builder_screen.blit(text, text_rect)

            if text_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                if clicked_pokemon_index != i:
                    choice = Pokemon(**data)
                    if player_team.get_team_len() < 6:
                        if choice not in player_team.get_team():
                            player_team.add_pokemon(choice)
                            added_pokemon.add(name)
                        else:
                            print('Pokemon already in your team ')
                    else:
                        print('Team is full ')

                    clicked_pokemon_index = i

        draw_team()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEWHEEL:
                scroll_position += event.y * 30

        pygame.display.update()
    pygame.quit()


team_builder()
