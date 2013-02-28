import os
import threading

import pygame
from pygame.locals import *

import Box2D

import event
import generator
import model.ship.human
import model.environment.space
import model.unit.human
    
class Game(Box2D.b2World, threading.Thread):

    def __init__(self):  
        
        # Initialize the thread
        threading.Thread.__init__(self)
        
         # Load pygame
        pygame.init()
        
        self._run = True
        
        self.event_handler = event.EventHandler()
        self.event_handler.start()
        
        # Register a quit event
        self.event_handler.register_event_listener(QUIT, self.quit)
    
        self.screen = pygame.display.set_mode((1024, 768))  
        self.meter_per_pixel = 1000 # 1 km per pixel
        
        # Set the game clock
        self.clock = pygame.time.Clock()  
        
        # Generates 10 humans    
        units = [model.unit.human.Human() for i in range(10)] 
        
        player = model.ship.human.Human(units)
        
        self.event_handler.register_event_listener(KEYDOWN, player.move_listener)
        self.event_handler.register_event_listener(KEYDOWN, player.attack_listener)
        
        # Current player
        self.player = player
        
        # Generator
        self.generator = generator.Generator()
        self.event_handler.register_event_listener(event.GENERATE, self.generator.generate_listener)
        self.generator.draw(self.screen)
           
        
    
    def run(self): 
        
        while self._run:        
            
            
            # Update the environment
            self.generator.update()

            # Draw shits
            pygame.display.flip()

            # limit the game to about 40fps, or 40 ticks per second.
            self.clock.tick(40) 
       
        
        pygame.quit()
        print "Main loop finished"
        
    def quit(self, event):
        """
        Quit the game.
        """
        self._run = False    
        self.event_handler._run = False           
    
            
    def box2d_to_screen_coordinates(self, x, y):
        return (x, y) / self.meter_per_pixel
    
    def screen_to_box2d_coordinates(self, x, y):
        return (x, y) * self.meter_per_pixel
       
        
    @classmethod
    def load_image(self, name, colorkey=None):
        fullname = os.path.join('asset/image', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print "Cannot load image:", name
            raise SystemExit, message
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image, image.get_rect()
    
    @classmethod
    def load_sound(self, name):
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print "Cannot load image:", name
            raise SystemExit, message
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image, image.get_rect()
