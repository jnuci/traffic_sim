class Entity:
    def __init__(self, position_x, position_y, velocity_x, velocity_y):
        self._position_x = position_x
        self._position_y = position_y
        self._velocity_x = velocity_x
        self._velocity_y = velocity_y
        self.ID = None

    def getPosition(self):
        return [self._position_x, self._position_y]
    
    def setPosition(self, pos):
        self._position_x = pos[0]
        self._position_y = pos[1]

    def getVelocity(self):
        return [self._velocity_x, self._velocity_y]
    
    def setVelocity(self, v):
        self._velocity_x = v[0]
        self._velocity_y = v[1]

    ## ID set by entityDB
    def getID(self):
        return self.ID