
from yahoo_finance import Share

class DataSource (object):
    def __init__(self,ticker):
        self.ticker = ticker
        self.stock = Share(self.ticker)

    def getPrice(self):
        return self.stock.get_price()

    def getName(self):
        return str(self.stock.data_set.get("Name"))

