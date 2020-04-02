import requests

def data_bbay():
    data = requests.get('https://bitbay.net/API/Public/BTCPLN/orderbook.json')
    return data.json()

def data_ticker_bbay():
    data_ticker = requests.get('https://bitbay.net/API/Public/BTCPLN/ticker.json')
    return data_ticker.json()

def data_trade_bchain():
    data_trade = requests.get('https://blockchain.info/ticker')
    return data_trade.json()

data = data_bbay()
data_tricker = data_ticker_bbay()
data_trade =data_trade_bchain()

buy_trade = trade['PLN']['buy']
sell_trade = trade['PLN']['sell']
buy_ticker_bbay = ticker['ask']
sell_ticker_bbay = ticker['bid']

asks_bbay = orderbook_bitbay['asks']
bids_bbay = orderbook_bitbay['bids']



