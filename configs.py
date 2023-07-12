import pygame
from pygame.locals import *

pygame.init()

class Window:
    WIDTH = 900
    HEIGHT = 500
    TITTLE ="Projeto Python"
    #ICON =

    @staticmethod
    def create():
        screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
        pygame.display.set_caption(Window.TITTLE)
        #pygame.display.set_icon(Window.ICON.convert_alpha())
        pygame.event.set_allowed([QUIT])

        return screen
    
pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))

class World:
    BACKGROUND = pygame.image.load("imgs/background.png").convert()
    FILL_BACKGROUND_COLOR = (255, 255, 255)

#class Skins:
        #HERO = pygame.image.load(f'imgs/idle/{i}.png')