from stockroom_manager import StockroomManager

class Stockroom:
    def __init__(self,stockroom_manger,product):
        self.__stockroom_manager=stockroom_manger
        self.__product=product
        
    def get_stockroom_manager(self):
        return self.__stockroom_manager
    
    def get_product(self):
        return self.__product
    
    def setter_stockroom_manager(self,stockroom_manger):
        self.__stockroom_manager=stockroom_manger
    
    def setter_product(self,product):
        self.__product=product

stockroom_manager1=StockroomManager(95412,"jose","nando",1155,"25-Jul-2022")
La_valle_stockroom=Stockroom(stockroom_manager1,"Telefono")
print(La_valle_stockroom.get_stockroom_manager())
"print(La_valle_stockroom.get_stockroom_manager.get_dni())"
"porque no se puede acceder a un atributo de stockroom manager? es porque lo hereda de otro?"
