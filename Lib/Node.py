from pygame.surface import Surface

class Node(object):
    def __init__(self) -> None:
        self.children = []
    def Update(self,surface:Surface)->None:
        for a in self.children:
            a.Update(surface)

    def AddChild(self,node)->None:
        self.children.append(node)

    
        
