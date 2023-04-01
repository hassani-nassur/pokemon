from Class.Fichier import *
from Class.Pockemone import Pockemone

class TypePockemone(Fichier,Pockemone):
    
    def __init__(self,name) -> None:
        
        Fichier.__init__(self)
        Pockemone.__init__(self,name)
        
        self.type_attaque = None
        self.type_defence = None
        data = self.get_data_files("db\pokedex.json")
        for i in  data:
            
            if(i['name']["french"] == name):
                
                self._puissance_attaque = i["base"]["Attack"]
                self._defence = i["base"]["Defense"]
                self._images = i["image"]
                self._type_names = i["type"]
            
        
        # self._resistance = resistance
        # self._faiblesse = faiblesse
    
    def get_type_names(self):
        return self._type_names
    def set_type_name(self,type_names):
        self._type_names = type_names
        
    def get_puissance_attaque(self):
        return self._puissance_attaque
    def set_puissance_attaque(self,attaque):
        self._puissance_atta = attaque  
    
    def set_type_attaque(self,type_attaque):
        self.type_attaque = type_attaque        
    def get_type_attaque(self):
        return self.type_attaque
    
    def set_type_defence(self,type_defence):
        self.type_defence = type_defence        
    def get_type_defence(self):
        return self.type_defence
    
    def get_point_life(self):
        return self._point_life 
       
    def set_point_life(self,point_life):
        self._point_life = point_life
    
    def set_defence(self,defence):
        self._defence = defence
    def get_defence(self):
        return self._defence
    
    def afficheInfo(self):
        text = "vies = {}\nDefence = {}\nattaque = {}".format(self._point_life,self._defence,self._puissance_attaque)
        return text
    