class inventory:
    current_inventory = []
    def __init__(self, name, quantity, description):
        self.name = name
        self.quantity = quantity
        self.description = description
        self.__class__.current_inventory.append(self)
