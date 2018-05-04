from ua.com.lviv.iot.Good import *


class Hammer(Good):
    def __init__(self, name="unknown", material="unknown", manufacturer="unknown", price=0, amount=0):
        super().__init__(self, name, material, manufacturer, price, amount)
        self.type = Types.HAMMER.name
