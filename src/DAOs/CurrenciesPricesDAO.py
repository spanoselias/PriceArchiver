import json
import traceback
import requests

def getCurrenciesPrice():
    url = "https://financialmodelingprep.com/api/v3/forex"
    r = requests.get(url)
    return json.loads(r.text)


def addHistoricalPrice(conn, pricesSchema, AddCurrencyPrice):
    # create a cursor
    cur = conn.cursor()

    insertSQL = "insert into %s.Currencies_Prices(" \
                "ticker, " \
                "bid, " \
                "ask," \
                "open, " \
                "high, " \
                "low, " \
                "changes, " \
                "date) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
 \
                (pricesSchema,
                 AddCurrencyPrice.ticker,
                 AddCurrencyPrice.bid,
                 AddCurrencyPrice.ask,
                 AddCurrencyPrice.open,
                 AddCurrencyPrice.low,
                 AddCurrencyPrice.high,
                 AddCurrencyPrice.changes,
                 AddCurrencyPrice.date)

    try:
        cur.execute(insertSQL)
        conn.commit()
    except:
        print("Error executing insert statement: error_messaage: " + str(traceback.print_exc()))
        conn.rollback()

    # close the communication with the PostgreSQL
    cur.close()
