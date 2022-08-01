class Spaceship:

    def __init__(self, model, type, manufacturer, description, stock_quantity, buying_cost, selling_price, id = None):
        self.model = model
        self.type = type
        self.manufacturer = manufacturer
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.id = id


    def mark_up(self):
        mark_up = round((self.selling_price - self.buying_cost) / self.buying_cost * 100, 2)
        return mark_up
        

