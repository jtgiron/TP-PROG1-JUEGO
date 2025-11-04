import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Sprite temporal (más adelante se reemplaza por animaciones)
        self.image = pygame.Surface((40, 60))
        self.image.fill((200, 80, 80))
        self.rect = self.image.get_rect(topleft=(x, y))

        # Físicas
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.jump_force = -15
        self.gravity = 0.8
        self.on_ground = False

    def update(self, keys):
        self.handle_input(keys)
        self.apply_gravity()

        # Movimiento horizontal
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def handle_input(self, keys):
        self.vel_x = 0
        if keys[pygame.K_a]:
            self.vel_x = -self.speed
        if keys[pygame.K_d]:
            self.vel_x = self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_force
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y += self.gravity
        if self.vel_y > 15:  # límite de caída
            self.vel_y = 15
