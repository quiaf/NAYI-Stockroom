from owner import Owner

class Headquater:
    """
high level support for doing this and that.
"""
    def __init__(self, name, cuit,building,owner):
        self.__name=name
        self.__cuit=cuit
        self.__building=building
        self.__owner=owner
    
    def get_name(self):
        return self.__name
        
    def get_cuit(self):
        return self.__cuit
    
    def get_building(self):
        return self.__building

    def get_owner(self):
        return self.__owner
    
    def setter_name(self,name):
        self.__name=name
        
    def setter_cuit(self,cuit):
        self.__cuit=cuit
    
    def setter_building(self,building):
        self.__building=building

    def setter_owner(self,owner):
        self.__owner=owner

owner1=Owner(233,"nayi","rojas",2355)
casaMatriz=Headquater("Avellaneda",233,"chs",owner1)
print(casaMatriz.get_owner().get_name())