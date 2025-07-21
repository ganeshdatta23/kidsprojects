import pygame

def simple_pygame_game():
    pygame.init()

    # Screen dimensions
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Simple Pygame Game")

    # Colors
    white = (255, 255, 255)
    red = (255, 0, 0)

    # Player properties
    player_size = 50
    player_x = (screen_width - player_size) // 2
    player_y = (screen_height - player_size) // 2
    player_speed = 5

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < screen_height - player_size:
            player_y += player_speed

        screen.fill(white)  # Fill the background
        pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size)) # Draw the player

        pygame.display.flip() # Update the display

    pygame.quit()

if __name__ == "__main__":
    simple_pygame_game()