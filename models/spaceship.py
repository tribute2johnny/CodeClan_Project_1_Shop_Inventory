class Spaceship:

    def __init__(self, model, type, description, stock_quantity, buying_cost, selling_price, id = None):
        self.model = model
        self.type = type
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.id = id