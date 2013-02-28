import pygame

import model
import model.unit

class Human(model.unit.Unit, pygame.sprite.Sprite):    
    """
    Defines a human.
    """
    
    def __init__(self, **attributes):
        
        model.Model.__init__(self, attributes)   
        
        
