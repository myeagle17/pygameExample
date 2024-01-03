import pygame, sys
from pygame.locals import *
from Engine import Engine
from Game.Player import Player

pygame.init();
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("TestGame")
engine = Engine(screen)
engine.AddNode(Player())
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    engine.Loop()
    pygame.display.update()
