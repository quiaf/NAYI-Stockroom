class Province:
    def __init__(self,name,country):
        self.__name=name
        self.__country=country

    def get_name(self):
        return self.__name
    
    def get_country(self):
        return self.__country

    def set_name(self,name):
        self.__name=name
    
    def set_country(self,country):
        self.__country=country