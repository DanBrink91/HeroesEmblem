import sys, pygame, os
from pygame.locals import *

class Unit(pygame.sprite.Sprite):
    dist = 31
    
    def __init__(self, art, x , y):
        pygame.sprite.Sprite.__init__(self)
        self.dist = Unit.dist
        
        self.x = x
        self.y = y

        self.image = pygame.image.load(art)
        self.rect = self.image.get_rect()
        

    def move_up(self):
        if self.y - self.dist >= 0:
            self.y -= self.dist

    def move_down(self):
        if self.y + self.dist <= 600 - self.dist:
            self.y += self.dist

    def move_right(self):
        if self.x + self.dist <= 900 - self.dist:
            self.x += self.dist

    def move_left(self):
        if self.x - self.dist >= 0:
            self.x -= self.dist 

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))