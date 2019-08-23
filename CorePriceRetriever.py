import _thread

from StocksPricesRetriever import PricesRetriever, HistoricalPricesRetriever

print('Retriever is running...')

try:
    p1 = _thread.start_new_thread(PricesRetriever.retrieveAndAddCurrentStockPrices, ("prices_archiver_debug",))
    p2 = _thread.start_new_thread(HistoricalPricesRetriever.retrieveAndAddHistoricalStockPrices,("prices_archiver_debug",))

except:
    print("Error: unable to start thread")

while 1:
    pass
