import pygame
from settings import *

# Inicializa Pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    running = True

    # Grupos de Sprites
    all_sprites = pygame.sprite.Group()
    player = Player(PLAYER_START_X, PLAYER_START_Y)
    all_sprites.add(player)

    # Bucle principal del juego
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar
        all_sprites.update()

        # Dibujar
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()


