import ability
import model

class Ship(model.Model, ability.Crew, ability.Battery):
    
    def __init__(self, units, attributes):
        """
        Attributes:
            speed
            acceleration
            energy
        """
        
        model.Model.__init__(self, attributes)
        ability.Battery.__init__(self, 100)
        ability.Crew.__init__(self, units)       
    