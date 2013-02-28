#
# Abilities
#
# These classes provides action to perform abilities.
#
#

import pygame

class Attack():
    
    def attack_listener(self, event):
        if event.key == pygame.K_LCTRL:
            self.attack()
    
    def attack(self):
        print "Attacking!"
        pass

class Defence():
    pass

class Battery():
    """
    Ability to have energy
    """
    
    def __init__(self, energy):
        self.energy = energy
    
    def dump_energy(self, battery, amount):
        """
        Dump the content of another storage object in this storage object
        """       
        
        if amount > battery.energy:
            amount = battery.energy
            print("Could not give more than {} J of energy, given {} instead".format(amount, battery.energy))
        
        battery.energy -= amount
        self.energy += amount  
        

class Crew():
    """
    Ability to carry a crew. Crew is a group of units.
    """
    
    def __init__(self, *units):
        
        self.units = units
        
    def dump_crew(self, crew, amount):
        """
        Dump the content of another storage object in this storage object
        """        
        while amount > 0:
            self.crew.append(crew.units.pop())
            amount -= 1
            
class Storage():
    
    def __init__(self, *materials):
        self.materials = materials
        
    def dump_storage(self, storage, amount):
        """
        Dump the content of another storage object in this storage object
        """        
        while amount > 0:
            self.materials.append(storage.materials.pop())
            amount -= 1
        
class Tank():
    """
    Ability to have fuel
    """
    
    def __init__(self, fuel):
        self.fuel = fuel
    
    def dump_fuel(self, tank, amount):
        """
        Dump the content of another storage object in this storage object
        """       
        
        if amount > tank.fuel:
            amount = tank.fuel
            print("Could not give more than {} J of energy, given {} instead".format(amount, energy.energy))
        
        tank.fuel -= amount
        self.fuel += amount    
        
class Move():
    """
    Ability to move. You should register the move function as a callback for
    KEYDOWN
    """   
        
    def move_listener(self, event):
        
        if event.key == pygame.K_UP:            
            self.move_up()
            
        if event.key == pygame.K_DOWN:
            self.move_down()
            
        if event.key == pygame.K_LEFT:
            self.move_left()
            
        if event.key == pygame.K_RIGHT:
            self.move_right()       
        
    
    def move_up(self):
        print "Moving up"
        
    
    def move_down(self):
        print "Moving down"
        
    def move_left(self):
        print "Moving left"
        
    def move_right(self):
        print "Moving right"
        
    
class Recruit():
    """
    Ability to recruit a unit in a crew
    """
    def recruit_unit(self, crew, unit_type, amount):
        
        # Purchase units
        crew.money -= unit_type.price * amount
        
        # Dump units in crew
        crew.dump_crew([unit_type() for i in range(amount)], amount)
        