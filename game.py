import pygame
from entities.player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.bg_color = (20, 20, 30)

        # Crear grupo de sprites
        self.all_sprites = pygame.sprite.Group()

        # Crear jugador
        self.player = Player(x=100, y=500)
        self.all_sprites.add(self.player)

    def update(self):
        keys = pygame.key.get_pressed()
        self.all_sprites.update(keys)
        self.keep_player_in_bounds()

    def draw(self):
        self.screen.fill(self.bg_color)
        self.all_sprites.draw(self.screen)

    def keep_player_in_bounds(self):
        """Evita que el jugador salga de la pantalla."""
        if self.player.rect.left < 0:
            self.player.rect.left = 0
        if self.player.rect.right > self.screen.get_width():
            self.player.rect.right = self.screen.get_width()
        if self.player.rect.bottom > self.screen.get_height():
            self.player.rect.bottom = self.screen.get_height()
            self.player.on_ground = True
        else:
            self.player.on_ground = False
