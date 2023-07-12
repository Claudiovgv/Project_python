import pygame
import os
from configs import *
from Orientation import *

class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.__alive = True
        self.__x = x
        self.__y = y
        self.__initial_y = y
        self.__jump_state = None
        self.__flip = False
        self.__animation_list = []
        self.__index = 0
        self.__action = 0
        self.__update_time = pygame.time.get_ticks()

        #load all image
        animation_types = ['idle', 'run', 'jump']
        for anamation in animation_types:
            temp_list = []
            #contar o numero de ficheiros numa pasta
            num_of_frames = len(os.listdir(f'imgs/{anamation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'imgs/{anamation}/{i}.png')
                temp_list.append(img)
            self.__animation_list.append(temp_list)

        self.__img = self.__animation_list[self.__action][self.__index]


    def draw(self, surface):
        surface.blit(pygame.transform.flip(self.__img, self.__flip, False), [self.__x, self.__y])

    def update_animation(self):
        #velocidade da animação
        ANIMATION_COOLDOWN = 80
        #update imagem 
        self.__img = self.__animation_list[self.__action][self.__index]
        #a ver quanto tempo passou desde o ultimo update
        if pygame.time.get_ticks() - self.__update_time > ANIMATION_COOLDOWN:
            #dar reset ao timer
            self.__update_time = pygame.time.get_ticks()
            #mudar de imagem
            self.__index += 1
        #dar reset assim que animação acabar
        if self.__index >= len(self.__animation_list[self.__action]):
            self.__index = 0

    def update_action(self, new_action):
        #verificar ação
        if new_action != self.__action:
            self.__action = new_action
            #update os setings da animação
            self.__index = 0
            self.__update_time = pygame.time.get_ticks()


    def move_left(self):
        self.__x -= 5
        self.__flip = True

        if self.__x < 10:
            self.__x = 10

    def move_right(self):
        self.__x += 5
        self.__flip = False

    def jump(self):
        if self.__jump_state != None:
            return

        self.__jump_state = Direction.RISING

    def update_jump(self):
        GRAVITY = 8
        MAX_JUMP = 150
        if self.__jump_state == Direction.RISING:
            self.__y -= 8
            if self.__y <= MAX_JUMP:
                self.__jump_state = Direction.FALLING
        elif self.__jump_state == Direction.FALLING:
            self.__y += GRAVITY
            if self.__y >= self.__initial_y:
                self.__y = self.__initial_y
                self.__jump_state = None