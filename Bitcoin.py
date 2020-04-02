import requests
import cs50 as cs

def data_bbay():
    data = requests.get('https://bitbay.net/API/Public/BTCPLN/orderbook.json')
    return data.json()

def data_ticker_bbay():
    data_ticker = requests.get('https://bitbay.net/API/Public/BTCPLN/ticker.json')
    return data_ticker.json()

def data_trade_bchain():
    data_trade = requests.get('https://blockchain.info/ticker')
    return data_trade.json()

def pierwsze_oferty(asks_bbay,bids_bbay):
    ilosc=cs.get_int("Ile ofert chcesz zobaczyć? : ")
    print("PIERWSZE",ilosc,"OFERT")
    print("CENA SPRZEDAŻY:")

    for i in range(ilosc):
        print(i+1,".",asks_bbay[i:i+1])

    print("CENA KUPNA:")
    for i in range(ilosc):
        print(i+1,".",bids_bbay[i:i+1])

def gdzie_kupic(buy_trade,buy_ticker_bbay,sell_trade,sell_ticker_bbay):
    if  buy_trade < buy_ticker_bbay:
        print("Lepiej kupić Bitcoin z Blokchain za", buy_trade,"zł")
    else:
        print("Lepiej kupić Bitcoin z Bitbay za", buy_ticker_bbay, "zł")

    if sell_trade > sell_ticker_bbay:
        print("Lepiej sprzedać Bitcoin z Blokchain za", sell_trade, "zł")
    else:
        print("Lepiej sprzedać Bitcoin z Bitbat za", sell_ticker_bbay, "zł")

data = data_bbay()
data_ticker = data_ticker_bbay()
data_trade =data_trade_bchain()

buy_trade = data_trade['PLN']['buy']
sell_trade = data_trade['PLN']['sell']
buy_ticker_bbay = data_ticker['ask']
sell_ticker_bbay = data_ticker['bid']
asks_bbay = data['asks']
bids_bbay = data['bids']

pierwsze_oferty(asks_bbay,bids_bbay)
print("-"*30)
gdzie_kupic(buy_trade,buy_ticker_bbay,sell_trade,sell_ticker_bbay)