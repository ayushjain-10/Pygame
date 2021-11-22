import pygame
from pygame.locals import *
pygame.init()

from GameObject import GameObject
from GameObject import Apple1
from GameObject import Apple2
from GameObject import Ghost
from GameObject import Ghost2
from GameObject import Player


screen = pygame.display.set_mode([500, 500])

frames_per_second = 30
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()
ghosts = pygame.sprite.Group()
apple1 = Apple1()
all_sprites.add(apple1)
fruit_sprites.add(apple1)
apple2 = Apple2()
all_sprites.add(apple2)
fruit_sprites.add(apple2)
ghost =  Ghost()
all_sprites.add(ghost)
ghost2 =  Ghost2()
all_sprites.add(ghost2)
ghosts.add(ghost)
ghosts.add(ghost2)
player = Player()
all_sprites.add(player)
score = 0

def get_collided_sprite(player, sprite_list):
    for sprite in sprite_list:
        if pygame.Rect.colliderect(player.rect, sprite.rect):
            return sprite

frame_counter = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()
    screen.fill((100, 200, 255))
    
    frame_counter += 1

    if frame_counter % 5 == 0:
        apple1.update()
        apple2.update()
        player.update()
        ghost.update()
        ghost2.update()

    apple1.move()
    apple2.move()
    ghost.move()
    ghost2.move()
    
    collided_fruit = get_collided_sprite(player, fruit_sprites)
    if collided_fruit:
        score += 1
        collided_fruit.speed += .01
        ghost.reset()
        ghost2.reset()
        while (get_collided_sprite(player, ghosts)) :
            ghost.reset()
            ghost2.reset()
        collided_fruit.reset()

    collided_ghost = get_collided_sprite(player, ghosts)
    if collided_ghost:
        running = False

    for sprite in all_sprites:
        sprite.render(screen)

    font = pygame.font.Font(None, 30)
    score_obj = font.render(f'Scoreboard: {score}', True, (100, 60, 255))
    screen.blit(score_obj, (350,20))

    pygame.display.flip()
    clock.tick(frames_per_second * 1.5)
