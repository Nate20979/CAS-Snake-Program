import pygame, os
from random import randint
from pygame.locals import *

def newpoint():
    return [randint(0, (win[0]-size)//size) * size, randint(0, (win[1]-size)//size) * size]

size = 10
ss = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

win = (800, 600)

pygame.init()

screen = pygame.display.set_mode(win)
pygame.display.set_caption('Snake')
screen.fill(BLACK)
pygame.display.flip()

snake = [[200, 200]]
surface = pygame.Surface(win, 0, 24)
clock = pygame.time.Clock()
clock.tick()

direction = ''
started = False

point = newpoint()

screen.fill(WHITE)

while True:
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if not started:
                started = True
            if e.key == K_ESCAPE:
                os._exit(0)
            elif e.key == K_UP:
                if direction != 'DOWN':
                    direction = 'UP'
            elif e.key == K_DOWN:
                if direction != 'UP':
                    direction = 'DOWN'
            elif e.key == K_LEFT:
                if direction != 'RIGHT':
                    direction = 'LEFT'
            elif e.key == K_RIGHT:
                if direction != 'LEFT':
                    direction = 'RIGHT'
        elif e.type == QUIT:
            os._exit(0)

    screen.fill(WHITE)

    if not started:
        pygame.display.flip()
        clock.tick(30)
        continue

    if len(snake) == ss:
        snake.pop()
    if direction == 'UP':
        snake.insert(0, [snake[0][0], snake[0][1]-size])
    elif direction == 'DOWN':
        snake.insert(0, [snake[0][0], snake[0][1]+size])
    elif direction == 'LEFT':
        snake.insert(0, [snake[0][0]-size, snake[0][1]])
    elif direction == 'RIGHT':
        snake.insert(0, [snake[0][0]+size, snake[0][1]])

    if snake[0][0] >= win[0] or snake[0][1] >= win[1] or snake[0][1] < 0 or snake[0][0] < 0:
        os._exit(0)

    for i in range(1, len(snake)):
        if snake[0] == snake[i]:
            os._exit(0)

    if snake[0] == point:
        ss += 1
        point = newpoint()
        print(ss-3)
        print(point)

    pygame.draw.rect(screen, RED, [point[0], point[1], size, size])

    for i in snake:
        pygame.draw.rect(screen, BLACK, [i[0], i[1], size, size])

    pygame.display.flip()
    clock.tick(30)
