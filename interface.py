import pygame

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

squirtle_health = 100
charmander_health = 100
HEALTH_BAR_WIDTH = 100
HEALTH_BAR_HEIGHT = 10

button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 80, 100, 40)


def draw_health_bar(screen, x, y, health):
    pygame.draw.rect(screen, RED, (x, y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
    pygame.draw.rect(screen, GREEN, (x, y, health, HEALTH_BAR_HEIGHT))


running = True

while running:
    screen.fill('lightblue')

    pygame.draw.ellipse(screen, (139, 69, 19), (100, 400, 200, 100))
    pygame.draw.ellipse(screen, (139, 69, 19), (500, 150, 200, 100))

    screen.blit(squirtle_back_img, enemy_pos)
    screen.blit(charmander_img, player_pos)

    draw_health_bar(screen, 150, 360, squirtle_health)
    draw_health_bar(screen, 545, 110, charmander_health)

    pygame.draw.rect(screen, RED, button_rect)
    font = pygame.font.Font(None, 30)
    text = font.render("Attack!", True, WHITE)
    screen.blit(text, (button_rect.x + 15, button_rect.y + 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Attack!")

    pygame.display.update()

# Quit Pygame
pygame.quit()
