import pygame, sys, os
from pygame.locals import *

pygame.init()
pygame.font.init()

def main():
    win = (600, 600)

    screen = pygame.display.set_mode(win, 0, 24)
    pygame.display.set_caption('Hello World')

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    myfont = pygame.font.SysFont(None, 48)
    text = myfont.render("Hello World!", 1, WHITE)
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, textRect)

    screen.blit(text, textRect)

    pygame.display.update()

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.quit()
                    quit()

main()

