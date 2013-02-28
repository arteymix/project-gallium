import pygame

import ability
import model.ship
import model.game

"""
Human ship
"""
class Human(model.ship.Ship, ability.Storage, ability.Attack, ability.Defence, ability.Move):
    
    def __init__(self, units, **attributes):
                
        model.ship.Ship.__init__(self, units, attributes)
        pygame.sprite.Sprite.__init__(self)
        
        # Load the image        
        self.image, self.rect = model.game.Game.load_image("ship/human.png")        
        
    
