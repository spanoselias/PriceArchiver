import datetime
from functools import reduce

from src.DAOs import StockPricesDBDAO
from src.Utils import DBUtils


def maxMinPricePerStock():
    stockPriceList = StockPricesDBDAO.getStockPrice(
        DBUtils.getPostgresConnection(),
        'pricesarchiver',
        datetime.datetime.utcnow() - datetime.timedelta(days=0.2))

    stockPricesList = stockPriceList
    maxStock = max(stockPricesList, key=lambda stock: stock.getPrice())
    minStock = min(stockPricesList, key=lambda stock: stock.getPrice())

    return maxStock, minStock

res = maxMinPricePerStock()
print(res)