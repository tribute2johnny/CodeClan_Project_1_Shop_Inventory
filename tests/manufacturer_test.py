import unittest

from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):

    def setUp(self):
        self.manufacturer = Manufacturer("Faulcon DeLacy", "description goes here", True)
        
    def test_manufacturer_has_name(self):
        self.assertEqual("Faulcon DeLacy", self.manufacturer.name)

    def test_manufacturer_has_description(self):
        self.assertEqual("description goes here", self.manufacturer.description)