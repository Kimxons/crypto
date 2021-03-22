import ccxt
import time

def getprice(symbol):
    symbol = input(symbol.upper()) #USDT/BTC
    sep = symbol.split("/")

    exchange = ccxt.binance({
        'enableRateLimits': True,
    })

    try:
        if(exchange.has['fetchTickers']):
            #if you want to fetch the whole binance data, ucomment this line
            # print(exchange.fetch_tickers())
            print(exchange.fetch_tickers(['ETH/BTC'])) #fetch minimal data on ETH

        #using fetchOHLCV / fetch_ohlcv to get the list of OHLCV candles for a particular symbol
        if (exchange.has['fetchOHLCV']):
            for symbol in exchange.markets:
                time.sleep(exchange.rateLimit / 1000)
                print(symbol, exchange.fetch_ohlcv(symbol, '1m')) #one minute
                
        if(exchange.has['fetchTrades']):
            for symbol in exchange.markets:
                print(symbol, exchange.fetch_trades(symbol))

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
print(getprice("Enter market symbol: "))