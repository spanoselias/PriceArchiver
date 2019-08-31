import time
import traceback

from src.Objects.AddCurrencyPrice import AddCurrencyPrice
from src.Utils import DBUtils
from src.DAOs import CurrenciesPricesDAO

def retrieveAndAddCurrenciesPrices(pricesSchema):
    print('retrieveAndAddHistoricalStockPrices is running...')
    while True:
        try:
            conn = DBUtils.getPostgresConnection()
            dic = CurrenciesPricesDAO.getCurrenciesPrice()
            for v in dic['forexList']:
                addCurrency = AddCurrencyPrice(v)

                CurrenciesPricesDAO.addHistoricalPrice(
                    conn,
                    pricesSchema,
                    addCurrency)

            time.sleep(5)

        except:
            print(traceback.print_exc())
