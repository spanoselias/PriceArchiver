class FetchStock:

    def __init__(self, resultset):
        self.symbol = resultset[0]
        self.price = resultset[1]
        self.date_added = resultset[2]

    def __repr__(self):
        return self.getSymbol() + ':' + str(self.getPrice())

    def getSymbol(self):
        return self.symbol

    def getPrice(self):
        return self.price

    def getDateAdded(self):
        return self.date_added
