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

<<<<<<< HEAD
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
=======
telefono1=Device("telefono","Samsung","S22")
print (telefono1.getType())
print (telefono1.getManufacturer())
print (telefono1.getModel())
telefono1.setType("Audifonos")
print (telefono1.getType())
telefono1.setManufacturer("Apple")
print (telefono1.getManufacturer())
telefono1.setModel("X21LL")
print (telefono1.getModel())
print(telefono1)
>>>>>>> develop
