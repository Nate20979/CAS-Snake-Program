#!/usr/bin/pythonw

import pygame, os
from random import randint
from pygame.locals import *


size = 15
ss = 5
win = (600, 600)
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 30)

screen = pygame.display.set_mode(win)
pygame.display.set_caption('Snake')
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
BRIGHTRED = (255, 0, 0)
BRGIHTGREEN = (0, 255, 0)
BRIGHTBLUE = (0, 0, 255)

surface = pygame.Surface(win, 0, 24)

def RandPoint():
    randpoint = randint(10, 20)
    return randpoint

def newpoint():
    return [randint(0, (win[0]-size)//size) * size, randint(0, (win[1]-size)//size) * size]

def main():

    size = 15
    ss = 5
    win = (600, 600)
    score = 0
    
    
    screen.fill(BLACK)
    pygame.display.flip()

    snake = [[300, 300]]
    clock = pygame.time.Clock()
    clock.tick()

    direction = 'NOTHING'
    started = False

    point = newpoint()
    randpoint = RandPoint()

    screen.fill(WHITE)
    
    isDead = False

    while True:
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if not started:
                    started = True
                if e.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                if e.key == K_p:
                    direction = 'PAUSED'
                elif e.key == K_UP:
                    if direction != 'DOWN':
                        direction = 'UP'
                elif e.key == K_DOWN:
                    if direction != 'UP':
                        direction = 'DOWN'
                elif e.key == K_RIGHT:
                    if direction != 'LEFT':
                        direction = 'RIGHT'
                elif e.key == K_LEFT:
                    if direction != 'RIGHT':
                        direction = 'LEFT'
            elif e.type == QUIT:
                pygame.quit()
                quit()

        screen.fill(WHITE)

        if not started:
            pygame.display.flip()
            clock.tick(15 + (ss-5)/5)
            continue
    
        if len(snake) == ss:
            snake.pop()
        if direction == 'UP':
            snake.insert(0, [snake[0][0], snake[0][1]-size])
        elif direction == 'DOWN':
            snake.insert(0, [snake[0][0], snake [0][1]+size])
        elif direction == 'LEFT':
            snake.insert(0, [snake[0][0]-size, snake[0][1]])
        elif direction == 'RIGHT':
            snake.insert(0, [snake[0][0]+size, snake[0][1]])
    
        if snake[0][0] >= win[0] or snake[0][1] >= win[1] or snake[0][1] < 0 or snake [0][0] < 0:
            isDead = True
    
        if ss-5 > randpoint:
            screen.fill(BLACK)
            scoreDisp = myfont.render(str(score), 1, (WHITE))
            screen.blit(scoreDisp, (10, 10))
            pygame.draw.rect(screen, BRIGHTBLUE, [point[0], point[1], size, size])
            for i in snake:
                pygame.draw.rect(screen, WHITE, [i[0], i[1], size, size])

        for i in range(1, len(snake)):
            if snake[0] == snake[i]:
                isDead = True
    
        if snake[0] == point:
            score += 10
            ss += 1
            point = newpoint()
            print(ss-5)
            print(point)

        if ss-5 <= randpoint:
            scoreDisp = myfont.render(str(score), 1, (BLACK))
            screen.blit(scoreDisp, (10, 10))
            pygame.draw.rect(screen, BRIGHTRED, [point[0], point[1], size, size])
            for i in snake:
                pygame.draw.rect(screen, BLACK, [i[0], i[1], size, size])
        
        if isDead == True:
            direction = 'NOTHING'
            if ss-5 <= 10:
                screen.fill(WHITE)
                label = myfont.render("Play Again?", 1, (BLACK))
                screen.blit(label, (250, 250))
                randpoint = RandPoint()
            if ss-5 > 10:
                screen.fill(BLACK)
                label = myfont.render("Play Again?", 1, (WHITE))
                screen.blit(label, (250, 250))
                randpoint = RandPoint()
            if e.type == KEYDOWN:
                if started == True:
                    started = False
                    isDead = False
                    direction = 'NOTHING'
                    snake = [[300, 300]]
                    ss = 5
                    point = newpoint()
                    score = 0


        pygame.display.flip()
        clock.tick(15 + (ss-5)/5)

main()

