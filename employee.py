from person import Person
class Employee(Person):
    def __init__(self,dni,name,last_name,telefono,hire_date):
        Person.__init__(self,dni,name,last_name,telefono)
        self.__hire_date=hire_date
    
    def get_hire_date(self):
        return self.__hire_date

    def setter_hire_date(self,hire_date):
        self.__hire_date=hire_date

employee1=Employee(95412,"jose","nando",1155,"25-Jul-2022")
print(employee1.get_dni())