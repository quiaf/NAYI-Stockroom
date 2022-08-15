from employee import Employee

class StockroomManager(Employee): 
    pass

stockroom_manager1=StockroomManager(95412,"jose","nando",1155,"25-Jul-2022")
print(stockroom_manager1.get_dni())