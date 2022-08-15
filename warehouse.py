from headquater import Headquater

class Warehouse(Headquater):
    def __init__(self, name, cuit, building, owner,product):
        super().__init__(name, cuit, building, owner)
        self.__product=product

    def get_product(self):
        return self.__product
    
    def set_product(self,product):
        self.__product=product