from headquater import Headquater

class Retail(Headquater):
    def __init__(self, name, cuit, building, owner,stockroom,employee):
        super().__init__(name, cuit, building, owner)
        self.__stockroom= stockroom
        self.__employee=employee

    
    def get_stockroom(self):
        return self.__stockroom

    def get_employee(self):
        return self.__employee
    
    
    def set_stockroom(self,stockroom):
        self.__stockroom= stockroom
    
    def set_employee(self,employee):
        self.__employee=employee