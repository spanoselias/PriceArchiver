class AddCurrencyPrice:

    def __init__(self, resultset):
        self.ticker = resultset['ticker']
        self.bid = resultset['bid']
        self.ask = resultset['ask']
        self.open = resultset['open']
        self.low = resultset['low']
        self.high = resultset['high']
        self.changes = resultset['changes']
        self.date = resultset['date']
