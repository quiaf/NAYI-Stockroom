from headquater import Headquater
from stockroom import Stockroom
from stockroom_manager import stockroom_manager1
from owner import owner1
from employee import employee1
from building import building1

class Retail(Headquater):
    def __init__(self, name, cuit, building, owner,stockroom_manager,product,employee):
        super().__init__(name, cuit, building, owner)
        self.__stockroom= Stockroom(stockroom_manager,product)
        self.__employee=employee

    
    def get_stockroom(self):
        return self.__stockroom

    def get_employee(self):
        return self.__employee
    
    
    def setter_stockroom(self,stockroom_manager,product):
        self.__stockroom= Stockroom(stockroom_manager,product)
    
    def setter_employee(self,employee):
        self.__employee=employee
    


retal1=Retail("9de Julio",165,building1,owner1,stockroom_manager1,"dell",employee1)
print(retal1.get_stockroom.get_stockroom_manager())