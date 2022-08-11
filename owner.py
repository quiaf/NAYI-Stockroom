from person import Person
class Owner(Person):
    def __init__(self,dni,name,last_name,telefono):
        super().__init__(dni,name,last_name,telefono)

owner1=Owner(586,"mari","melendez",5545)
print(owner1.get_dni())