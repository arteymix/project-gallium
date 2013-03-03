import pygame

class Generator(pygame.sprite.Group):
    """
    Map generator.
    """
    top_index = 0
    right_index = 0
    
    def generate_listener(self, event):
        pass
    
    def generate(self, posx, posy):
        
        piece_of_space = space.Space()
        
        piece_of_space.rect.topleft = (posx, posy)
        
        self.add(piece_of_space)
        
        print "Added a piece of space"

    