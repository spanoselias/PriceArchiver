import json
import traceback

import requests

def getSymbols():
    url = "https://financialmodelingprep.com/api/v3/company/stock/list"
    r = requests.get(url)
    return json.loads(r.text)

def getSymbolsPrices():
    url = "https://financialmodelingprep.com/api/v3/stock/real-time-price"
    r = requests.get(url)
    return json.loads(r.text)

def addSymbol(conn, pricesSchema, symbol, symbolName, price):
    # create a cursor
    cur = conn.cursor()

    addSymbolSQL = \
        "insert into %s.Symbols(symbol, name, price) values('%s', '%s', '%s')" % \
        (pricesSchema, symbol, symbolName, price)

    try:
        cur.execute(addSymbolSQL)
        conn.commit()
    except:
        print("Error executing insert statement")
        conn.rollback()

    # close the communication with the PostgreSQL
    cur.close()

def addSymbolPrice(conn, pricesSchema, symbol, price, date_added):
    # create a cursor
    cur = conn.cursor()

    insertSQL = \
        "insert into %s.StocksPrices(symbol, price, date_added) values('%s', '%s', '%s')" % \
        (pricesSchema, symbol, price, date_added)

    try:
        cur.execute(insertSQL)
        conn.commit()
    except:
        print('Error while adding the symbol price: ' + traceback.print_exc())
        conn.rollback()

    # close the communication with the PostgreSQL
    cur.close()
