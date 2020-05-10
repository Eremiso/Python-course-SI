import requests
import pandas as pd

def currency_names():
    currency_name = ['BTC', 'ETH', 'LTC', 'XRP', 'BCH']
    return currency_name

def price(Currency):
    data = requests.get("https://www.bitstamp.net/api/v2/ticker/{}{}/".format(Currency.lower(), 'usd')).json()['bid']
    return float(data)

def price_day_ago(Currency):
    data = requests.get("https://www.bitstamp.net/api/v2/transactions/{}{}/".format(Currency.lower(), 'usd'),params={'time': 'day'}).json()[-1]['price']
    return float(data)

def edit_data():

    print("Insert cryptocurrency(BTC/ETH/LTC/XRP/BCH) that you want to change: ")
    currency = input()
    while currency.upper() not in currency_names():
        print("Incorrect cryptocurrency, try again")
        currency = input()

    print("Insert new amount")
    amount = float(input())
    while amount < 0:
        print("Incorrect valume, try again")
        amount = float(input())

    data.at[data['Currency'] == currency.upper(), 'Amount'] = amount
    data.to_csv('wallet.csv', index=False)
    print("Changes safe")

def currency_variables ():
    print("Working...")
    data['My Value'] = round(data['Currency'].apply(price) * data['Amount'], 1)
    data['My Value day ago'] = round(data['Currency'].apply(price_day_ago) * data['Amount'], 1)
    data['Value'] = round(data['Currency'].apply(price), 1)
    data['Value day ago'] = round(data['Currency'].apply(price_day_ago), 1)
    data['Profit'] = round(data['My Value'] - data['My Value day ago'],1)
    return data

def sum_usd():

    sum=0
    data['My Value'] = round(data['Currency'].apply(price) * data['Amount'], 1)
    for i in range(len(data['Currency'])):
        sum += data['My Value'][i]
    return round(sum,2)

def menu():

    key = int(input())

    if key == 1:
        edit_data()
        print(20 * '-')
    elif key == 2:
        print(data)
        print(20*'-')
    elif key == 3:
        print(currency_variables())
        print(60 * '-')
    elif key == 4:
        print("You have",sum_usd(),"USD in crypto currencies")
        print(20*'-')
    elif key == 5:
        exit("Closing...")


print("Welcome in super_fajna_aplikacja")
while True:
    data = pd.read_csv('wallet.csv')

    print("1) Edit wallet")
    print("2) Check wallet")
    print("3) Currency variables")
    print("4) Sum value in USD")
    print("5) Close app")

    menu()

