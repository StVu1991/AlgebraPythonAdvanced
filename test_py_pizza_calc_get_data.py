from unittest import TestCase
from py_pizza_calc_get_data import GetPPCData

class TestGetPPCData(TestCase):
    def test_get_toppings(self):
        result = GetPPCData.get_toppings()
        self.assertIn("Chicken", result)

    de