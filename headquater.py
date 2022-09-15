class Headquater:
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
    
    def set_name(self,name):
        self.__name=name
        
    def set_cuit(self,cuit):
        self.__cuit=cuit
    
    def set_building(self,building):
        self.__building=building

    def set_owner(self,owner):
        self.__owner=owner