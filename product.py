class Product:
    def __init__(self,serial,product_type,model,manufacturer,price):
        self.__serial=serial
        self.__model=model
        self.__product_type=product_type
        self.__manufacturer=manufacturer
        self.__price=price

    def get_serial (self):
        return self.__serial

    def get_model (self):
        return self.__model

    def get_product_type(self):
        return self.__product_type
    
    def get_manufacturer(self):
        return self.__manufacturer

    def get_price(self):
        return self.__price

    def set_serial (self,serial):
        self.__serial=serial

    def set_model (self,model):
        self.__model=model

    def set_product_type(self,product_type):
        self.__product_type=product_type
    
    
    def set_manufacturer(self,manufacturer):
        self.__manufacturer=manufacturer

    def set_price(self,price):
        self.__price=price
