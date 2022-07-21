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