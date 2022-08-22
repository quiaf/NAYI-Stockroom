class Person:

    def __init__(self,dni,name,last_name,telephone):
        self.__dni=dni
        self.__name=name
        self.__last_name=last_name
        self.__telephone=telephone

    def get_dni(self):
        return self.__dni   

    def get_name(self):
        return self.__name 

    def get_last_name(self):
        return self.__last_name

    def get_telephone(self):
        return self.__telephone

    def set_dni(self,dni):
        self.__dni=dni 

    def set_name(self,name):
        self.__name=name

    def set_last_name(self,last_name):
        self.__last_name=last_name

    def set_telephone(self,telephone):
        self.__telephone=telephone