class Product:
    def __init__(self,type,model,price):
        self.__model=model
        self.__type=type
        self.__price=price
    
    def get_model (self):
        return self.__model

    def get_type(self):
        return self.__type
    
    def get_price(self):
        return self.__price
    
    def setter_model (self,model):
        self.__model=model

    def setter_type(self,type):
       self.__type=type
    
    def setter_price(self,price):
        self.__price=price

product1=Product("30-55","telefono",233.22)
print(product1.get_price())