class Product:
    def __init__(self,product_type,model,manufacturer,price):
        self.__model=model
        self.__product_type=product_type
        self.__manufacturer=manufacturer
        self.__price=price
    
    def get_model (self):
        return self.__model

    def get_product_type(self):
        return self.__product_type
    
    def get_manufacturer(self):
        return self.__manufacturer

    def get_price(self):
        return self.__price
    
    def setter_model (self,model):
        self.__model=model

    def setter_product_type(self,product_type):
        self.__product_type=product_type
    
    
    def setter_manufacturer(self,manufacturer):
        self.__manufacturer=manufacturer

    def setter_price(self,price):
        self.__price=price
