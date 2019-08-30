import json
import traceback
import requests


def getHistoricalPrice(symbol):
    url = "https://financialmodelingprep.com/api/v3/historical-price-full/%s" % symbol
    r = requests.get(url)
    return json.loads(r.text)


def addHistoricalPrice(conn, pricesSchema, symbol, open, high, low, changePercent, date):
    # create a cursor
    cur = conn.cursor()

    insertSQL = "insert into %s.StocksHistoricalPrices(symbol, open, high, low, change_percent, date) values('%s', '%s', '%s', '%s', '%s', '%s')" % \
                (pricesSchema, symbol, open, high, low, changePercent, date)

    try:
        cur.execute(insertSQL)
        conn.commit()
    except:
        print("Error executing insert statement: error_messaage: " + str(traceback.print_exc()))
        conn.rollback()

    # close the communication with the PostgreSQL
    cur.close()
