class Device:
    def __init__(self,type,manufacturer,model):
        self.__type=type
        self.__manufacturer=manufacturer
        self.__model=model
    def getType(self):
        return self.__type
    def getManufacturer(self):
        return self.__manufacturer
    def getModel(self):
        return self.__model
    def setType(self,type):
        self.__type=type
    def setManufacturer(self,manufacturer):
        self.__manufacturer=manufacturer
    def setModel(self,model):
        self.__model=model
class Stockroom:
    def __init__(self,stockroomID,stockroomName,address,province,city):
        self.__stockroomID=stockroomID
        self.__stockroomName=stockroomName
        self.__address=address
        self.__province=province
        self.__city=city
    def getStocktoomID(self):
        return self.__stockroomID
    def getStockroomName(self):
        return self.__stockroomName
    def getAddress(self):
        return self.__address
    def getProvince(self):
        return self.__province
    def getCity(self):
        return self.__city
    def setStockroomID(self,ID):
        self.__stockroomID=ID
    def setStockroomName(self,stockroomName):
        self.__stockroomName=stockroomName
    def setAddress(self,address):
        self.__address=address
    def setProvince(self,province):
        self.__province=province
    def setCity(self,city):
        self.__city=city


class empleado:
    def __init__(self,DNI,name,lastName,storeID):
        self.__DNI=DNI
        self.__name=name
        self.__lastName=lastName
        self.__storeID=storeID
    def getDNI(self):
        return self.__DNI
    def getName(self):
        return self.__name
    def getLastName(self):
        return self.__lastName
    def getStoreID(self):
        return self.__storeID
    def setDNI(self,DNI):
        self.__DNI=DNI
    def setDNI(self,DNI):
        self.__DNI=DNI
    def setDNI(self,DNI):
        self.__DNI=DNI
    def setDNI(self,DNI):
        self.__DNI=DNI