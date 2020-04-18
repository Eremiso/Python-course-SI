import requests

def data():
    data=[]
    buy=[]
    sell=[]
    name=[]

    data.append(requests.get('https://bitbay.net/API/Public/BTC/USD/ticker.json').json())
    data.append(requests.get("https://blockchain.info/ticker").json())
    data.append(requests.get('https://www.bitstamp.net/api/ticker').json())
    data.append(requests.get('https://cex.io/api/ticker/BTC/USD').json())

    name=["Bitbay","Blocchain","Bitstamp","Cex"]

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

    taker=[0.003,0.024,0.025,0.03]
    for i in range(len(taker)):
        sell.append((sell[i]-(taker[i]*sell[i])))

    return  buy,sell,name

def buy_and_sell(data):

    buy_best=max(zip(data[0],data[2]))
    sell_best=max(zip(data[1],data[2]))

    return buy_best,sell_best

print(buy_and_sell(data()))