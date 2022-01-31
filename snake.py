import random
import pygame
from pygame.locals import *

def grid():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def colisão(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

count = 0

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0,0,255))

maça_pos = grid()
maça = pygame.Surface((10, 10))
maça.fill((255, 0, 0))

direção = LEFT
clock = pygame.time.Clock()

while True:
    clock.tick(15 + count)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direção = UP
            if event.key == K_DOWN:
                direção = DOWN
            if event.key == K_RIGHT:
                direção = RIGHT
            if event.key == K_LEFT:
                direção = LEFT

    if colisão(snake[0], maça_pos):
        count += 1
        maça_pos = grid()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i-1][0], snake[i-1][1]

    if direção == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direção == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direção == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direção == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((34, 139, 34))
    screen.blit(maça, maça_pos)
    for pos in snake:
        screen.blit(snake_skin ,pos)

    txt = f'Points: {count}'
    pygame.font.init()                            
    fonte = pygame.font.get_default_font()          
    fontesys = pygame.font.SysFont(fonte, 40)          
    txttela = fontesys.render(txt, 1, (255,255,255)) 
    screen.blit(txttela,(252,25))                   

    pygame.display.update() 