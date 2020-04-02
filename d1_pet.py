class Pet(object):

    def __init__(self, name = "", kind = ""):
"""Ge objektet dess egenskaper."""
        self.name = name
        self.kind = kind
        self.toy = []

    def add_toy(self, toy):
"""Lägg till toy till listan self.toy om den inte redan finns."""
        if toy in self.toy:
            pass
        else:
            self.toy.append(toy)

    def __str__(self):
"""Retunera en sträng som beskriver instansen."""
        if self.toy == []:
            return "{} är en {} som inte har några leksaker".format(self.name,
                                                                    self.kind)
        else:
            return"{} är en {} som har följande leksaker: ".format(
                                                        self.name, self.kind)
                                                        + ", ".join(self.toy)
