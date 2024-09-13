import pygame
# Initialize Pygame
pygame.init()

# Define the screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Create the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokemon Battle Layout")

# Load Pokemon images (make sure these paths are correct) (download pokemons)
squirtle_img = pygame.image.load("squirtle.png")
squirtle_back_img = pygame.image.load("squirtleback.png")
charmander_img = pygame.image.load("charmander.png")
bulbasaur_img = pygame.image.load("bulbasaur.png")

# Scale the Pokemon images to fit the platforms (still have to download the pokemons)
squirtle_img = pygame.transform.scale(squirtle_img, (100, 100))
charmander_img = pygame.transform.scale(charmander_img, (100, 100))
bulbasaur_img = pygame.transform.scale(bulbasaur_img, (100, 100))

# Define the health values (we'll simulate static health bars for now)
squirtle_health = 100
charmander_health = 100

# Health bar dimensions (change these according to lukas)
HEALTH_BAR_WIDTH = 100
HEALTH_BAR_HEIGHT = 10

# Define button dimensions and position (for attack etc)
button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 80, 100, 40)

# Function to draw health bars
def draw_health_bar(screen, x, y, health):
    pygame.draw.rect(screen, RED, (x, y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))  # Background (red)
    pygame.draw.rect(screen, GREEN, (x, y, health, HEALTH_BAR_HEIGHT))  # Health (green)

# Main loop
running = True
while running:
    # Fill the background with green
    screen.fill(GREEN)

    # Draw the platforms (as ovals)
    pygame.draw.ellipse(screen, (139, 69, 19), (100, 400, 200, 100))  # Left oval platform (Squirtle)
    pygame.draw.ellipse(screen, (139, 69, 19), (500, 150, 200, 100))  # Right oval platform (Charmander)

    # Blit (draw) the Pokémon images on the screen
    screen.blit(squirtle_back_img, (155, 380))  # Position Squirtle on the left platform
    screen.blit(charmander_img, (550, 120))  # Position Charmander on the right platform

    # Draw health bars above each Pokémon
    draw_health_bar(screen, 130, 330, squirtle_health)  # Squirtle's health bar
    draw_health_bar(screen, 530, 80, charmander_health)  # Charmander's health bar

    # Draw the attack button
    pygame.draw.rect(screen, DARK_RED, button_rect)
    font = pygame.font.Font(None, 30)
    text = font.render("Attack!", True, WHITE)
    screen.blit(text, (button_rect.x + 10, button_rect.y + 5))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the attack button is clicked
            if button_rect.collidepoint(event.pos):
                print("Attack!")  # Placeholder action for the attack

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()