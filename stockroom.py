class Stockroom:
    def __init__(self,stockroom_manger,product):
        self.__stockroom_manager=stockroom_manger
        self.__product=product
        
    def get_stockroom_manager(self):
        return self.__stockroom_manager
    
    def get_product(self):
        return self.__product
    
    def set_stockroom_manager(self,stockroom_manger):
        self.__stockroom_manager=stockroom_manger
    
    def set_product(self,product):
        self.__product=product