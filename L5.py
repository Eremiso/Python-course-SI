import time
import requests

def database():
    data = []
    value_ask = []
    value_bid = []
    name = ["BTC","ZEC","ETH","LTC","DASH"]

    data.append(requests.get('https://bitbay.net/API/Public/BTC/USD/ticker.json').json())
    data.append(requests.get('https://bitbay.net/API/Public/ZEC/USD/ticker.json').json())
    data.append(requests.get('https://bitbay.net/API/Public/ETH/USD/ticker.json').json())
    data.append(requests.get('https://bitbay.net/API/Public/LTC/USD/ticker.json').json())
    data.append(requests.get('https://bitbay.net/API/Public/DASH/USD/ticker.json').json())

    for i in range(len(data)):
        value_bid.append(data[i]['bid'])
        value_ask.append(data[i]['ask'])

    return value_ask, value_bid, name

def sort(data):
    for i in range(len(data)):
        x = len(data) - 1
        while x > i:
            if data[x] < data[x - 1]:
                z = data[x]
                data[x] = data[x - 1]
                data[x - 1] = z
            x=x-1
    data.reverse()
    return data

def percent_print(function):
    ask,bid,name=function
    percent_tab=[]
    dict={}
    for i in range(len(name)):
        percent=(ask[i]-bid[i])/(ask[i])
        percent=round(percent*100,2)
        add={percent:name[i]}
        dict.update(add)
        percent_tab.append(percent)

    percent_tab = sort(percent_tab)

    for i in range(len(percent_tab)):
        print(dict[percent_tab[i]],percent_tab[i],"%")

while True:
    percent_print(database())
    print("Refreshing...")
    time.sleep(300)
