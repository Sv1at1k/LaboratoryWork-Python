class HypermarketManager:
    goodList = []

    def add_good(self, good):
        self.goodList.append(good)

    def what_buy(self, price):
        result = []
        for good in self.goodList:
            if good.price < price:
                result.append(good)
        return result

    def find_type(self, type):
        result = []
        for good in self.goodList:
            if good.type == type:
                result.append(good)
        return result
