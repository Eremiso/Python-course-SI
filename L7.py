import matplotlib.pyplot as plt
import random
import json
import requests
from copy import *

def data_input():
    input_tab = []
    tab_currency = ["btc", "eth", "ltc"]
    currency = input("którą kryptowalutę chcesz sprawdzić: BTC, ETH, LTC: ").lower()

    while currency not in tab_currency:
        print("nie obsługiwana kryptowaluta :( , wprowadz ponownie")
        currency = input("którą kryptowalutę chcesz sprawdzić: BTC, ETH, LTC: ").lower()

    input_tab.append(currency)
    print(40 * "-")
    print("symulacja będzie trwać 30dni i zacznie się pierwszego dnia miesiąc")
    year = str(input("podaj rok w którym chcesz przeprowadzić symulację: "))
    print(40 * "-")
    month = int(input("podaj miesiąc w którym chcesz przeprowadzić symulację (np: 10, 01): "))

    while month>12:
        print("nie ma takiego miesiąca :( , wprowadz jeszcze raz")
        month= int(input("podaj miesiąc w którym chcesz przeprowadzić symulację(np: 10, 01): "))

    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)

    start = year + '-' + month + '-01'
    input_tab.append(start)

    return input_tab # 0-currency 1-start

def get_data_from_request(input_tab):
    request = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol="+input_tab[0]+"&market=USD&apikey=DQHTDT7WB9NVTARN").json()
    data = json.dumps(request, sort_keys=(True), indent=4)
    data = json.loads(data)
    data = data['Time Series (Digital Currency Daily)']

    list_data = list(data.keys())
    list_price = []

    for i in range(len(list_data)):
        list_price.append(float(data[list_data[i]]['4a. close (USD)']))

    data = []
    price = []
    for i in range(len(list_data)):
        if input_tab[1] == list_data[i]:
            data.append(list_data[i:i + 30])
            price.append(list_price[i:i + 30])
    data = data[0]
    price = price[0]

    tab_from_request=[]
    tab_from_request.append(data)
    tab_from_request.append(price)
    tab_from_request.append(list_data)
    tab_from_request.append(list_price)

    return tab_from_request #0-data, 1-price, 2-lista_data, 3-lista_price

def pred(tab_from_request):
    predict = []

    for i in range(len(tab_from_request[2])):
        if tab_from_request[2][i] == tab_from_request[0][0]:
            before = tab_from_request[3][i-1]

    for i in range(len(tab_from_request[1]) - 1):
        if i == 0:
            diff = tab_from_request[1][i] - before
            diff = diff * random.random() * 2
            rand = random.random()

            if rand > 0.2:
                predict.append(tab_from_request[1][-1] + diff)
            else:
                predict.append(tab_from_request[1][-1] - diff)
        else:
            diff = tab_from_request[1][i+1] - tab_from_request[1][i]
            diff = diff * random.random() * 2
            rand = random.random()

            if rand > 0.2:
                predict.append(predict[i - 1] + diff)
            else:
                predict.append(predict[i - 1] - diff)

    diff = predict[0] - tab_from_request[1][-1]
    diff = diff * random.random() * 2
    rand = random.random()

    if rand > 0.2:
        predict.append(predict[-1] + diff)
    else:
        predict.append(predict[-1] - diff)

    return predict

def pred_100(tab_from_request):
    list_pred = []
    predict = []
    for i in range(100):
        list_pred.append(pred(tab_from_request))

    for i in range(len(list_pred[0])):
        help = []
        for j in range(len(list_pred)):
            help.append(list_pred[j][i])
        predict.append(sum(help) / len(list_pred))
    return predict

def wykresy(days, price, price_100):
    plt.figure()
    plt.plot(days, price)
    plt.title("1 symulacja")
    plt.figure()
    plt.plot(days, price_100)
    plt.title("średnia ze 100 symulacji")

    plt.show()

input_tab = data_input()

predict = pred(get_data_from_request(input_tab))
predict_100 = pred_100(get_data_from_request(input_tab))

price = get_data_from_request(input_tab)[1]
price_100 = copy(price)

for i in range(len(predict)):
    price.append(predict[i])
    price_100.append(predict_100[i])

days = []

for i in range(60):
    days.append(-30+i)

wykresy(days, price, price_100)

print(40*"-")