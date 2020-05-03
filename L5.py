import time
import requests

def data():
    data = []
    value_ask = []
    value_bid = []

    data.append(requests.get('https://bitbay.net/API/Public/BTC/USD/ticker.json').json())
    data.append(requests.get('https://bitbay.net/API/Public/ZEC/USD/ticker.json').json())
    data.append(requests.get('https://bitbay.net/API/Public/ETH/USD/ticker.json').json())
    data.append(requests.get('https://bitbay.net/API/Public/LTC/USD/ticker.json').json())
    data.append(requests.get('https://bitbay.net/API/Public/DASH/USD/ticker.json').json())

    for i in range(len(data)):
        value_bid.append(data[i]['bid'])
        value_ask.append(data[i]['ask'])

    return value_ask, value_bid