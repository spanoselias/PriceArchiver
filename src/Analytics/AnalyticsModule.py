import datetime

from src.DAOs import StockPricesDBDAO
from src.Utils import DBUtils


def maxPricePerStock():
    stockPriceList = \
        StockPricesDBDAO.getStockPrice(
            DBUtils.getPostgresConnection(),
            'pricesarchiver',
            datetime.datetime.utcnow() - datetime.timedelta(days=0.1))
