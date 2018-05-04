from ua.com.lviv.iot.Types import Types


class Good:

    def __init__(self, name="unknown", material="unknown", manufacturer="unknown", price=0, amount=0):
        self.manufacturer = manufacturer
        self.name = name
        self.material = material
        self.amount = amount
        self.price = price
        self.type = Types.GOOD.name

    def to_string(self):
        return "Type:", self.type , " Name:" , self.name , " Material:" , self.material , " Manufacturer:" , self.manufacturer , " Price:", self.price, " Amount:", self.amount
