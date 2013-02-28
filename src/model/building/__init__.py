import model

"""
Base class for buildings
"""
class Building(model.Model):
    
    
    def __init__(self, units, ships, attributes):            
        
        # Apply attributes to model
        model.Model.__init__(self, attributes)
        
        self.units = units
        self.ships = ships
        
		