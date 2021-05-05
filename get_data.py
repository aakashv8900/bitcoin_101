import config, csv
from binance.client import Client
client = Client(config.API_KEY, config.API_SECRET)


#prices = client.get_all_tickers()
#for price in prices:
#    print(price)

candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")


csvfile = open('main.csv', 'w', newline='')
candelstick_writer = csv.writer(csvfile, delimiter=',')


for candle in candles:
    print(candle)
    candelstick_writer.writerow(candle)

print(len(candles))