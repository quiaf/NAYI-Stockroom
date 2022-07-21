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
    def __init__(self,stockroomID,stockroomName):
        self.__stockroomID=stockroomID
        self.__stockroomName=stockroomName
    