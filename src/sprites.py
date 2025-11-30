import pygame


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/spaceship.png")
        rect = self.image.get_rect()
        rect.width = width
        rect.height = height
        self.rect = self.image.get_rect()
        self.velocity = 5
        self.cooldown = 1000
        self.last_shot = 0
        self.bullets = pygame.sprite.Group()

    def move(self, vect):
        self.rect.x += vect
        screen_rect = pygame.Rect((0, 0), pygame.display.get_window_size())
        self.rect.clamp_ip(screen_rect)

    def user_movement(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.move(self.velocity)
        if pressed[pygame.K_LEFT]:
            self.move(-self.velocity)

    def shoot(self):
        time = pygame.time.get_ticks()
        if time - self.last_shot >= self.cooldown:
            self.last_shot = time
            self.bullets.add(Bullet(5, self.rect.center))

    def update(self) -> None:
        self.user_movement()
        self.shoot()
        self.bullets.update()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, position) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4, 15))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=position)
        self.speed = speed

    def update(self) -> None:
        screen_dims = pygame.display.get_window_size()
        self.rect.y -= self.speed
        if self.rect.y < 0 or self.rect.y >= screen_dims[1]:
            self.kill()


class Alien(pygame.sprite.Sprite):
    def __init__(self, type, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f"assets/alien_{type}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
