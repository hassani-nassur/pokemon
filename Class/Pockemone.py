class Pockemone:
    
    def __init__(self,name):
        self._name = name
        self._point_life = 100
        
    def setName(self,name):
        self._name = name
    def get_name(self):
        return self._name
    
    