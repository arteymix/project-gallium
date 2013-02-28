
import pygame
import model
import Box2D

class Environment(model.Model):
    """
    Environment.

    An environment could be space, or around a planet.
    Environments contains ships.
    """
    
    def __init__(self, attributes):
        
        model.Model.__init__(self, attributes)
        

            
        