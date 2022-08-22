from person import Person
class Employee(Person):
    def __init__(self,dni,name,last_name,telefono,hire_date):
        super().__init__(dni,name,last_name,telefono)
        self.__hire_date=hire_date
    
    def get_hire_date(self):
        return self.__hire_date

    def set_hire_date(self,hire_date):
        self.__hire_date=hire_date
