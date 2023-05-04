import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((300, 300))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        screen.fill((0, 255, 255))
        pygame.display.flip()

if __name__ == '__main__':
    main()