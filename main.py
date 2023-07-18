import pygame
import time
import sys
from configs import *
from Main_caracter import *
from pygame.locals import *

pygame.init()

screen = Window.create()

player = Hero(10, 378, 1.5)
background_x = 0



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
        idling = True
            #controlo de teclas no jogo
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            player.update_action(1)
            player.move_left()
            idling = False

        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            player.update_action(1)
            player.move_right()    
            idling = False


        if key[pygame.K_w] or key[pygame.K_UP]:
            player.jump()
            player.update_action(2)
            idling = False
        if idling:
            player.update_action(0)

        player.update_jump()

    if player.get_x() >= 800:
        player.set_x(800)  # Limita a posição da personagem em 800 pixels

        if player.get_x() > Window.WIDTH / 2 + 200 and (key[pygame.K_d] or key[pygame.K_RIGHT]):
            if background_x > Window.WIDTH - World.BACKGROUND.get_width():
                background_x -= 3

    elif player.get_x() <= 50:
        player.set_x(50)  # Limita a posição da personagem em 50 pixels

        if player.get_x() < Window.WIDTH / 2 - 200 and (key[pygame.K_a] or key[pygame.K_LEFT]):
            if background_x < 0:
                background_x += 3


    #desenhar o fundo
    screen.blit(World.BACKGROUND, [background_x, 0])
    
    player.update_animation()
    player.draw(screen)


    #apresentar frame
    pygame.display.update()

pygame.quit()