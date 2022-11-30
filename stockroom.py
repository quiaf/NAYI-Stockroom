from employee import Employee

class Stockroom:
    def __init__(self,employee,product):
        self.__employee=employee
        self.__product=product
        
    def get_employee(self):
        return self.__employee
    
    def get_product(self):
        return self.__product
    
    def set_employee(self,employee):
        self.__employee=employee
    
    def set_product(self,product):
        self.__product=product
        
    def assign_stockroom_manager(self,employee):
        if employee.is_stockroom_manager():
            self.__employee=employee
        else:
            print("This user cann't be assigned to this stockroom")
    
    def has_stockroom_manager(self):
        return self.__employee!= None
    
    
    def remove (self,stockroom_manager):


        



    def hasStockroomManager(stockroom_manger):
