class City:
    def __init__(self,name,province,neighborhood):
        self.__name=name
        self.__province=province
        self.__neighborhood=neighborhood
    
    def set_name(self):
        return self.__name
    
    def set_province(self):
        return self.__province
    
    def set_neighborhood(self):
        return self.__neighborhood
    
    def get_name(self,name):
        self.__name=name
    
    def get_province(self,province):
        self.__province=province

    def get_neighborhood(self,neighborhood):
        self.__neighborhood=neighborhood