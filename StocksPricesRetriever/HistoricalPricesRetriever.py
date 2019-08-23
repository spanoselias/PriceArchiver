import time
import traceback

from StocksPricesRetriever import StockPricesDAO, DBUtils, HistoricalStockPricesDAO


def retrieveAndAddHistoricalStockPrices(pricesSchema):
    print('retrieveAndAddHistoricalStockPrices is running...')
    try:
        conn = DBUtils.getPostgresConnection()
        dic = StockPricesDAO.getSymbols()
        for v in dic['symbolsList']:
            symbol = v['symbol']

            historicalPricesForGivenSymbol = {}
            try:
                try:
                    historicalPricesForGivenSymbol = HistoricalStockPricesDAO.getHistoricalPrice(symbol)
                except:
                    print(traceback.print_exc())
                    time.sleep(180)
                    while len(historicalPricesForGivenSymbol) == 0:
                        try:
                            historicalPricesForGivenSymbol = HistoricalStockPricesDAO.getHistoricalPrice(symbol)
                        except:
                            print(traceback.print_exc())
                            time.sleep(30)

                for v in historicalPricesForGivenSymbol['historical']:
                    HistoricalStockPricesDAO.addHistoricalPrice(
                        conn,
                        pricesSchema,
                        symbol,
                        v['open'],
                        v['high'],
                        v['low'],
                        v['changePercent'],
                        v['date'])

                time.sleep(5)

            except:
                print(traceback.print_exc())

    except:
        print(traceback.print_exc())
        conn.close()
