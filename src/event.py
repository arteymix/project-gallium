import threading

import pygame

# Defined event in the game
GENERATE = "GENERATE" # Include a x and y position to generate
UPDATE = "UPDATE"
    
class EventHandler(threading.Thread):
    """
    Async event handler
    """
    def __init__(self):
        
        # Initialize the thread
        threading.Thread.__init__(self)
        
        # Dict where keys are events
        self._run = True
        self.listeners = {}
        self.clock = pygame.time.Clock()
    
    def run(self):
        while self._run:
            events = pygame.event.get() 

            for event in events:   
                for callback in self.listeners.get(event.type, []):
                    callback(event)

            self.clock.tick(40)
        
        print "Event handler finished"
        
    def register_event_listener(self, type, callback):   
                
        if type not in self.listeners.keys():
            self.listeners[type] = []
            
        self.listeners[type].append(callback)   
