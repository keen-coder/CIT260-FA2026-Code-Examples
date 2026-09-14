import math

class Circle:

    def __init__(self, radius=1.0):
    
        #self.__radius = radius
        self.set_radius(radius)
   
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius=1.0):
        
        if radius < 0:
            raise ValueError('Error: Radius cannot be negative')
        else:
            self.__radius = radius
        
        
        
        if radius < 0:
            print('Error: Radius cannot be negative')
            print('Radius not changed.')
        else:
            self.__radius = radius

    def area(self):
        return self.__radius**2 * math.pi
    
    def circumference(self):
        return 2 * self.__radius * math.pi
    
    def __str__(self):
        return f'Circle: {{radius = {self.get_radius()}}}'