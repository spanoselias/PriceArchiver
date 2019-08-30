class FetchStock:

    def __init__(self, resultset):
        self.symbol = resultset[0]
        self.price = resultset[1]
        self.date_added = resultset[2]

    def __get_symbol(self):
        return self.symbol

    def __get_price(self):
        return self.price

    def __get_date_added(self):
        return self.date_added
