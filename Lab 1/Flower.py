class Flower:
    totalAmount = 0

    def __init__(self, name="default", price=0, amount=0, color="default", rate=0):
        self.name = name
        self.price = price
        self.amount = amount
        self.color = color
        self.rate = rate
        Flower.totalAmount += amount

    def to_string(self):
        print("Name:" + self.name + "; Price:", self.price,
              "; Amount:", self.amount, "; Color:" + self.color + "; Rate:", self.rate, ";")

    def print_sum(self):
        print("Кількість " + self.name, self.amount)

    @staticmethod
    def print_static_sum():
        print("Загальна кількість",Flower.totalAmount)


if __name__ == '__main__':
    flower = Flower("Ромашка", 32, 32, "red", 10)
    flowerBasic = Flower()
    flower4 = Flower("Ромашка", 6586732, 1323, "blue")
    flower.to_string()
    flowerBasic.to_string()
    flower4.to_string()
    flower.print_sum()
    flowerBasic.print_sum()
    flower4.print_sum()
    Flower.print_static_sum()


