class Item:
    def __int__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "weight": self.weight,
        }
