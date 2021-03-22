import ccxt

def getprice(symbol):
    symbol = symbol.upper()
    sep = symbol.split("/")

    exchange = ccxt.binance({
        'enableRateLimits': True,
    })

    markets = exchange.load_markets()
    #print(exchange.id, "\n", markets)

    try:
        price = exchange.fetch_ticker(symbol)
        fprice = price['info']['lastPrice']
        if(sep[1] == "USD" or sep[1] == 'USDT'):
            pprice = "{:.2f} {}".format(float(fprice),sep[1])
            return pprice
        else:
            pprice = "{:.8f} {}".format(float(fprice),sep[1])
            return pprice
    except (ccxt.ExchangeError, ccxt.NetworkError) as error:
        return 'Found an error', type(error).__name__, error.args
    raise
print(getprice("btc/usdt"))
