class Person:

    def __init__(self,dni,name,last_name,telefono):
        self.__dni=dni
        self.__name=name
        self.__last_name=last_name
        self.__telefono=telefono

    def get_dni(self):
        return self.__dni   

    def get_name(self):
        return self.__name 

    def get_last_name(self):
        return self.__last_name

    def get_telefono(self):
        return self.__telefono

    def setter_dni(self,dni):
        self.__dni=dni 

    def setter_name(self,name):
        self.__name=name

    def setter_last_name(self,last_name):
        self.__last_name=last_name

    def setter_telefono(self,telefono):
        self.__telefono=telefono