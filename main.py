import pygame
from game import Game

def main():
    pygame.init()
    pygame.display.set_caption("Dead Cells Clone")
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    game = Game(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update()
        game.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
