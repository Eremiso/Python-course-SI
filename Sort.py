from numpy import *

def tab_liczb():
    tab=[]
    rozmiar = int(input("wprowadz wielkość tabeli"))
    for i in range(rozmiar):
        liczba=int(input("wprowadz liczbę"))
        tab.append(liczba)
    return tab

def sort_bobmelkowe(tab):
    for i in range(len(tab)):
        x = len(tab) - 1
        while x > i:
            if tab[x] < tab[x - 1]:
                z = tab[x]
                tab[x] = tab[x - 1]
                tab[x - 1] = z
            x=x-1
    return tab

def sort_wstawianie(tab):
    for i in range(1,len(tab)):
        x = tab[i]
        j = i - 1
        while j>=0 and tab[j]>x:
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j + 1] = x
    return tab

tab=tab_liczb()
print("sortowanie bombelkowe",sort_wstawianie(tab))
print("sortowanie przez wstawianie",sort_bobmelkowe(tab))
