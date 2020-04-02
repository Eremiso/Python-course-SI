import requests

def bitbay_data():
    data = requests.get('https://bitbay.net/API/Public/BTCPLN/orderbook.json')
    return data.json()

def bitbay_data_ticker():
    data_ticker = requests.get('https://bitbay.net/API/Public/BTCPLN/ticker.json')
    return data_ticker.json()

def data_trade_bchain():
    data_trade = requests.get('https://blockchain.info/ticker')
    return data_trade.json()
