
import pygame
from fenrir.game.overworld.Spritesheet import Spritesheet

class overworld_npc:
    def __init__(self, x, y, filename):
        self.__x = x
        self.__y = y
        self.__sprite = pygame.image.load(filename)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite):
        self.__sprite = sprite