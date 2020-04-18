import requests

def data():
    data=[]
    buy=[]
    sell=[]

    data.append(requests.get('https://bitbay.net/API/Public/BTC/USD/ticker.json').json())
    data.append(requests.get("https://blockchain.info/ticker").json())
    data.append(requests.get('https://www.bitstamp.net/api/ticker').json())
    data.append(requests.get('https://cex.io/api/ticker/BTC/USD').json())

    buy.append(data[0]['ask'])
    sell.append(data[0]['bid'])
    buy.append(data[1]["USD"]["buy"])
    sell.append(data[1]["USD"]["sell"])
    buy.append(float(data[2]['ask']))
    sell.append(float(data[2]['bid']))
    buy.append(data[3]['ask'])
    sell.append(data[3]['bid'])

    # prowizja taker moze się zmieniać.
    # 0 = bitbay, 1 = blockchain, 2 = bitstamp, 3 = cex

    taker=[1.03,1.024,1.025,1.03]

    return  buy,sell,taker

print(data()[0])