import csv
from position import Position
from data_source import DataSource

class Portfolio(object):

    def __init__(self):
        csvFile = "/Users/jamesjirgens/PycharmProjects/mine_graphed/resources/portfolio.csv"
        prtfReader = csv.DictReader(open(csvFile))

        self.positions = []

        for row in prtfReader:
            stock = DataSource(row["instrument"])
            position = Position(row["instrument"], row["quantity"], stock.getName(), stock.getPrice() )
            self.positions.append(position)


    def getPositions(self):
        return self.positions


