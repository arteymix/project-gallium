#
# Abilities
#
# These classes provides action to perform abilities.
#
#

import pygame

import ability

class Ability():
    """
    Base class to define an ability
    """
    def update(self):
        """
        Hook to update specific hability
        """
        pass

class Attack(ability.Ability):
    
    def attack_listener(self, event):
        if event.key == pygame.K_LCTRL:
            self.attack()
    
    def attack(self, defend):
        # Apply the attack on the ennemy armor
        defend.defend(self)
        

class Defend(ability.Ability):
    """
    Ability to defend from an attack
    """
    def defend(self, attack):
        self.armor -= attack.damage
    
class Purchase(ability.Ability):
    
    def purchase(self, money):
        pass

class Battery(ability.Ability):
    """
    Ability to have energy
    """
        
    def dump_energy(self, battery, amount):
        """
        Dump the content of another storage object in this storage object
        """       
        
        if amount > battery.energy:
            amount = battery.energy
            print("Could not give more than {} J of energy, given {} instead".format(amount, battery.energy))
        
        battery.energy -= amount
        self.energy += amount
        
    def update(self):          
                            
        # Consume energy for that delta of time, in a frictionless environment
        # no energy is mathematically consumed
        self.energy -= self.linearVelocity *  Game.environment.friction * delta
        
        # Consume energy due to acceleration
        self.energy -= 0.5 * self.weight * math.abs(self.speed - last_speed)**2
        

class Crew(ability.Ability):
    """
    Ability to carry a crew. Crew is a group of units.
    """     
    
    def dump_crew(self, crew, amount):
        """
        Dump the content of another storage object in this storage object
        """        
        while amount > 0:
            self.units.append(crew.units.pop())
            amount -= 1
            
class Store(ability.Ability):
    """
    Ability to store minerals
    """
        
    def store(self, storage, amount):
        """
        Dump the content of another storage object in this storage object
        """        
        while amount > 0:
            self.materials.append(storage.materials.pop())
            amount -= 1
            
class Repair(ability.Ability, ability.Store):
    """
    Use minerals to repair armor
    """
    
    def repair(self, defend, amount):
        
        if self.minerals < amount:
            amount = self.minerals
            
        self.minerals -= amount        
        defend.defence += amount
    
        
class Tank(ability.Ability):
    """
    Ability to have fuel
    """
    
    def dump_fuel(self, tank, amount):
        """
        Dump the content of another storage object in this storage object
        """       
        
        if amount > tank.fuel:
            amount = tank.fuel
            print("Could not give more than {} J of energy, given {} instead".format(amount, energy.energy))
        
        tank.fuel -= amount
        self.fuel += amount    
        
class Move(ability.Ability):
    """
    Ability to move. You should register the move function as a callback for
    KEYDOWN
    """
    
    def update(self):
        """
        As it can move, update the object based on its physics defined by box2d
        """        
        
        # Update internal clock and apply relativists effects
        last_speed = self.attributes["speed"]
        delta = -(self.clock.get_time() - self.tick()) / 1000
        
        # Update the sprite from the physical positions (center and angle)      
        self.rect.center = Game.box2d_to_screen_coordinate(self.GetWorldPoint(self.localCenter))
        
        # Update the sprite rotation
        pygame.transform.rotate(self, self.angle)
        
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
        
    
        
    
class Recruit(ability.Ability):
    """
    Ability to recruit a unit in a crew
    """
    def recruit_unit(self, crew, unit_type, amount):
        
        # Purchase units
        crew.money -= unit_type.price * amount
        
        # Dump units in crew
        crew.dump_crew([unit_type() for i in range(amount)], amount)
        