class Devices:
    def __init__(self,type,manufacturer,model):
        self.__type=type
        self.__manufacturer=manufacturer
        self.__model=model
    def getType(self):
        return self.__type