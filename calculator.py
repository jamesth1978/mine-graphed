from pprint import pprint


def calcTotalValue(position):

    pprint(position)
    if (position.price is not None and position.quantity is not None):
        position.totalValue = float(position.quantity) * float(position.price)
