import pytest
from stockroom import Stockroom
from product import Product

def stockroom_manager_test(self):

    stockroom1=Stockroom("Maria","telefono")
    self.assertEqual(stockroom1.get_stockroom_manager,"Maria")


