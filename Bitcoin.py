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
        print(asks_bbay[i:i+1])

    print("CENA KUPNA:")
    for i in range(ilosc):
        print(bids_bbay[i:i+1])

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