__author__="guillaume"
__date__ ="$2013-02-28 00:00:59$"

import Box2D
import pygame

class Model(pygame.sprite.Sprite, Box2D.b2Body):
    
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
   
        
    def attack(self, other):
        other.armor -= self.attack
        
    def update(self):
        
        # Update the sprite from the physical positions (center and angle)      
        self.rect.center = Game.box2d_to_screen_coordinate(self.GetWorldPoint(self.localCenter))
        pygame.transform.rotate(self.angle)
        
        last_speed = self.attributes["speed"]
        delta = -(self.clock.get_time() - self.tick()) / 1000       

        # Update speed       
       
        
                
        # Consume energy for that delta of time, in a frictionless environment
        # no energy is mathematically consumed
        self.energy -= self.linearVelocity *  Game.environment.friction * delta
        
        # Consume energy due to acceleration
        self.energy -= 0.5 * self.weight * math.abs(self.speed - last_speed)**2
        
                
