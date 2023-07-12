import pygame
import time
import sys
from configs import *
from Main_caracter import *
from pygame.locals import *

pygame.init()

screen = Window.create()

player = Hero(10, 330)

clock = pygame.time.Clock()
while 1:
    dt = clock.tick(60)

    #evento para fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #mapear todas a teclas
    key = pygame.key.get_pressed()

    #para controlar quando o player morrer
    if player.alive:
            #controlo de teclas no jogo
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            player.update_action(1)
            player.move_left()
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            player.update_action(1)
            player.move_right()
        elif key[pygame.K_w] or key[pygame.K_UP]:
            player.jump()
            player.update_action(2)
        else:
            player.update_action(0)

        player.update_jump()


    #desenhar o fundo
    screen.blit(World.BACKGROUND, [0, 0])
    
    player.update_animation()
    player.draw(screen)


    #apresentar frame
    pygame.display.update()

pygame.quit()