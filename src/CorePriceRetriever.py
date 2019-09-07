import _thread

from src import PricesRetriever, CurrenciesPricesRetriever

print('Retriever is running...')

try:
    t1 = _thread.start_new_thread(PricesRetriever.retrieveAndAddCurrentStockPrices, ("pricesarchiver",))
    # t2 = _thread.start_new_thread(HistoricalPricesRetriever.retrieveAndAddHistoricalStockPrices,("pricesarchiver",))
    t3 = _thread.start_new_thread(CurrenciesPricesRetriever.retrieveAndAddCurrenciesPrices, ("pricesarchiver",))

except:
    print("Error: unable to start thread")

while True:
    pass
