

class Position(object):
    def __init__(self, name, quantity, ticker, price):
        self.name = name
        self.quantity = quantity
        self.ticker = ticker
        self.price = price
        self.totalValue = 0


    def getName(self):
        return self.name

    def getQuantity(self):
        return self.quantity

    def getTicker(self):
        return self.ticker

    def getPrice(self):
        return self.price

    def __repr__(self):
        return (self.name + " " + self.ticker + " " + self.quantity)