import pygame
import model
import model.environment
import model.game

class Space(model.environment.Environment):
    
    def __init__(self, **attributes):
        model.environment.Environment.__init__(self, attributes)
        pygame.sprite.Group.__init__(self)
        
        # Load the image        
        self.image, self.rect = model.game.Game.load_image("environment/space.png") 
    
  
      
    
