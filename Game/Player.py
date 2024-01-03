import pygame
from pygame.locals import *
from pygame.surface import Surface
from Lib.Node import Node

class Player(Node):
    img:Surface
    def __init__(self) -> None:
        super().__init__()
        self.img = pygame.image.load("./logo.png").convert_alpha()
        self.x = 0
        self.y = 0

    def Update(self,surface:Surface) -> None:
        super().Update(surface)
        # for event in pygame.event.get():
        #     if event.type == pygame.KSCAN_A:
        #         self.x = self.x+1
        if pygame.key.get_pressed()[pygame.K_a]:
            self.x = self.x+1
        surface.blit(self.img,(self.x,self.y))

        