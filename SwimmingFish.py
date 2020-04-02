import random
import sys, pygame
from pygame.locals import *
from Fish import *

pygame.init()
screen_info = pygame.display.Info()
screen_size = (screen_info.current_w, screen_info.current_h)

# set width and height to size of screen
size = (width, height) = (int(screen_info.current_w / 2), int(screen_info.current_h / 2))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 255)  # blue
fishes = []

def main():
    for i in range(10):
        fishes.append(Fish((width / 2, height / 2)))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                fishes.append(Fish(event.pos))
            if event.type == KEYDOWN:
                if event.key == K_d:
                    for i in range(len(fishes) // 2):
                        fishes.pop(0)
                if event.key == K_f:
                    pygame.display.set_mode(screen_size, FULLSCREEN)
                if event.key == K_ESCAPE:
                    pygame.display.set_mode(size)
        screen.fill(color)
        for fish in fishes:
            fish.update()
            fish.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
