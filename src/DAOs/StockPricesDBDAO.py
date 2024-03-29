import datetime
import traceback

from src.Utils import DBUtils
from src.Objects.FetchStock import FetchStock


def getStockPrice(conn, pricesSchema, date_added):

    fetchQuery = \
        "select symbol, price, date_added from %s.StocksPrices where date_added >= '%s'" % \
        (pricesSchema, date_added)

    try:
        resultList = DBUtils.executeSelectQuery(conn, fetchQuery, FetchStock)

    except:
        print(traceback.print_exc())
        conn.rollback()

    return resultList




