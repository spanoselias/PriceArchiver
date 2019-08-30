import datetime
import json
import traceback
import requests

from StocksPricesRetriever.Utils import DBUtils
from StocksPricesRetriever.src.Objects.FetchStock import FetchStock


def getStockPrice(conn, pricesSchema, date_added):
    # create a cursor
    cur = conn.cursor()

    fetchQuery = \
        "select symbol, price, date_added from %s.StocksPrices where date_added >= '%s'" % \
        (pricesSchema, date_added)

    stockPricesList = []
    try:
        cur.execute(fetchQuery)
        rs = cur.fetchall()

        for row in rs:
            stockPriceRow = FetchStock(row)
            stockPricesList.append(stockPriceRow)

    except:
        print(traceback.print_exc())
        conn.rollback()

    return stockPricesList


stockPriceList = getStockPrice(DBUtils.getPostgresConnection(), 'pricesarchiver',
                               datetime.datetime.utcnow() - datetime.timedelta(days=0.1))
print(len(stockPriceList))
