__author__="guillaume"
__date__ ="$2013-02-28 00:00:59$"

import Box2D
import pygame

import ability
import game
import model

class Model(pygame.sprite.Sprite, Box2D.b2Body):
    """
    Defines a generic game model
    """
    
    def __init__(self, attributes):
        """
        attributes:
            speed: in m/s
            acceleration: in m/s2
            friction: 
            maniability: in rad/s
            fuel: in L
            price: in $
            storage: in kg
            energy: in J
            attack:
            armor:
            weight: in kg
        """        
       
        pygame.sprite.Sprite.__init__(self)
        
        # Update internal dict with attributes
        self.__dict__.update(attributes)      
        
        # Setup internal clock
        self.clock = pygame.time.Clock()
        
        # Load image
        
        # Load the image        
        self.image, self.rect = game.Game.load_image("ship/human.png")  
              
    def update(self): 
        """
        Triggers an update for all inherited abilities
        """
        
        print "updating"
                       
        # Update abilities (will update Moving speed, and energy and other abilities like that)        
        for ability in self.__bases__:
            if isinstance(ability, ability.Ability):
                ability.update(self)        
        
                
class Unit(model.Model):
    
    def __init__(self, **attributes):
        model.Model.__init__(self, attributes)
        
        # load image        
    

class Environment(model.Model):
    
    def __init__(self, **attributes):
        model.Model.__init__(self, attributes)
    


class Ship(model.Model, ability.Crew, ability.Battery, ability.Move, ability.Attack):
    
    def __init__(self, **attributes):
        """
        Attributes:
            speed
            acceleration
            energy
        """
        
        model.Model.__init__(self, attributes)            
    

class Building(model.Model, ability.Crew):
    pass