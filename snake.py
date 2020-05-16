import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,290)
    y = random.randint(0,290)
    #fazer uma divisão inteira por 10 e multiplicar por 10
    return (x//10 * 10, y//10 * 10)
    #gera uma localização mutipla de 10 pra botar a maçã

def collision(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Snake by Victor N.')

#o corpo da cobra é uma tupla (começa com 3 endereços, seções)
snake = [(200, 200), (210, 200), (220, 200)]
#definição do que é formado o corpo da cobra
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

#posição aletória pra maçã
apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

#controle do FPS
clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if event.type == KEYDOWN:
        if event.key == K_UP:
            my_direction = UP
        if event.key == K_RIGHT:
            my_direction = RIGHT
        if event.key == K_DOWN:
            my_direction = DOWN
        if event.key == K_LEFT:
            my_direction = LEFT

    #se há a colisão, a maçã vai pra cauda da cobra
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    #FPS
    pygame.display.update()