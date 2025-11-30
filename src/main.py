# Example file showing a basic pygame "game loop"
import pygame
import sprites


def create_aliens(rows=5, columns=11):
    global aliens_sprites
    window_height = 720
    window_width = 1920
    aliens_sprites.empty()  # clear existing aliens if needed

    # Get alien sprite size (assuming all types have the same size)
    sample_alien = sprites.Alien(1, 0, 0)
    alien_width = sample_alien.rect.width
    alien_height = sample_alien.rect.height

    # Calculate horizontal and vertical spacing dynamically
    h_spacing = (window_width - alien_width * columns) // (columns)
    v_spacing = (window_height // 2 - alien_height * rows) // (
        rows + 1
    )  # top half of screen

    for row in range(rows):
        for column in range(columns):
            # Determine alien type based on row
            if row == 0:
                alien_type = 3
            elif row in (1, 2):
                alien_type = 2
            else:
                alien_type = 1

            # Calculate position dynamically
            x = h_spacing + column * (alien_width + h_spacing)
            y = v_spacing + row * (alien_height + v_spacing)

            alien = sprites.Alien(alien_type, x, y)
            aliens_sprites.add(alien)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_sprites = pygame.sprite.Group()
spaceship = sprites.Spaceship("green", 100, 100)
spaceship.rect.x = screen.get_width() // 2
spaceship.rect.y = screen.get_height() - 100
player_sprites.add(spaceship)

aliens_sprites = pygame.sprite.Group()
create_aliens()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    player_sprites.update()
    aliens_sprites.update()
    player_sprites.draw(screen)
    aliens_sprites.draw(screen)
    spaceship.bullets.draw(screen)
    for bullet_sprite in spaceship.bullets:
        hit = pygame.sprite.spritecollide(bullet_sprite, aliens_sprites, True)
        if hit:
            bullet_sprite.kill()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
