class Building:
    def __init__(self,name, address,postal_code,neighborhood):
        self.__name=name
        self.__address=address
        self.__postal_code=postal_code
        self.__neighborhood=neighborhood

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_postal_code(self):
        return self.__postal_code
    
    def get_neighborhood(self):
        return self.__neighborhood

    def setter_name(self,name):
        self.__name=name
    
    def setter_address(self,address):
        self.__address=address
    
    def setter_postal_code(self,postal_code):
        self.__postal_code=postal_code
    
    def setter_neighborhood(self,neighborhood):
        self.__neighborhood=neighborhood
