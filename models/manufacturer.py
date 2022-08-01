class Manufacturer:

    def __init__(self, name, description, active = True, id = None):
        self.name = name
        self.description = description
        self.active = active
        self.id = id

    def deactivate(self):
        self.active = False