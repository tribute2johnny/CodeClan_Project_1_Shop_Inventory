import unittest

from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):

    def setUp(self):
        self.manufacturer = Manufacturer("Faulcon DeLacy")
        
    def test_manufacturer_has_name(self):
        self.assertEqual("Faulcon DeLacy", self.manufacturer.name)