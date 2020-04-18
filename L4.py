import requests
import time

def data():
    data=[]
    buy=[]
    sell=[]

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
        sell[i]=(sell[i]-(taker[i]*sell[i]))

    return  buy,sell,name


def arbitration(data,amount):

    buy_best=min(zip(data[0],data[2]))
    sell_best=max(zip(data[1],data[2]))
    index_buy=data[2].index(buy_best[1])+1
    index_sell=data[2].index(sell_best[1])+1

    if buy_best<sell_best:
        resources_file = open('C:/Users/Legion/Desktop/Python-course-SI/resources.txt', 'r+')
        resources = resources_file.readlines()
        income = (sell_best[0] - buy_best[0]) * amount
        print("NA GIEŁDZIE",buy_best[1],"MOŻNA KUPIĆ",amount,"ZA USD PO KURSIE",buy_best[0],"I SPRZEDAĆ NA GIEŁDZIE",sell_best[1],"PO KURSIE", sell_best[0],"ZYSKUJĄC",income,"USD")
        if float(resources[(index_sell * 5) + 1]) > amount and float(resources[(index_buy * 5) - 1]) > sell_best[0] * amount:
            resources[1] = str(float(resources[1]) + income) + "\n"
            resources[(index_sell * 5) + 1] = str(float(resources[(index_buy * 5) + 1]) - amount) + "\n"
            resources[(index_buy * 5) + 1] = str(float(resources[(index_buy * 5) + 1]) + amount) + "\n"
            resources[(index_sell * 5) - 1] = str(float(resources[(index_sell * 5) - 1]) + sell_best[0] * amount) + "\n"
            resources[(index_buy * 5) - 1] = str(float(resources[(index_buy * 5) - 1]) - buy_best[0] * amount) + "\n"
            resources_file.seek(0)
            resources_file.writelines(resources)
        else:
            print("NIE WYSTARCZAJĄCE ILOŚĆ ŚRODKÓW NA KONCIE")
        resources_file.close()
    else:
        print("ARBITRAŻ NIE MOŻLIWY")
        print("NAJELPSZE CENY TERAZ ZA",amount,"BTC")
        print("ABY KUPIĆ",buy_best[0]*amount,"USD  NA",buy_best[1])
        print("ABY SPRZEDAĆ",sell_best[0]*amount,"USD  NA",sell_best[1])

amount=0.1
while True:
    dane = data()
    arbitration(dane, amount)
    print('-'*40)
    time.sleep(5)