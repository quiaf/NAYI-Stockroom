class City:
    def __init__(self,name,province):
        self.__name=name
        self.__province=province
    
    def set_name(self):
        return self.__name
    
    def set_province(self):
        return self.__province
    
    def get_name(self,name):
        self.__name=name
    
    def get_province(self,province):
        self.__province=province
