import unittest

from models.spaceship import Spaceship

class TestSpaceship(unittest.TestCase):

    def setUp(self):
        self.spaceship = Spaceship("Python", "Multipurpose", "Lakon Spaceways", "description goes here", 10, 690800, 999600)

    def test_spaceship_has_model(self):
        self.assertEqual("Python", self.spaceship.model)

    def test_spaceship_has_type(self):
        self.assertEqual("Multipurpose", self.spaceship.type)

    def test_spaceship_has_description(self):
        self.assertEqual("description goes here", self.spaceship.description)

    def test_spaceship_has_stock_quantity(self):
        self.assertEqual(10, self.spaceship.stock_quantity)

    def test_spaceship_has_buying_cost(self):
        self.assertEqual(690800, self.spaceship.buying_cost)

    def test__spaceship_has_selling_price(self):
        self.assertEqual(999600, self.spaceship.selling_price)