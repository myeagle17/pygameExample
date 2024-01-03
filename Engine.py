import pygame, sys
from pygame.locals import *
from pygame.surface import Surface
from Lib.Node import Node

class Engine(object):
    root:Node
    screen:Surface
    def __init__(self,screen) -> None:
        self.root = Node()
        self.screen = screen

    def Init(self):
        print("engine init")

    def Loop(self):
        print("Loop")
        self.root.Update(self.screen)  
    def AddNode(self,node)->None:
        self.root.AddChild(node)