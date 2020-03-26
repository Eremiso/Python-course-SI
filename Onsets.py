from numpy import *

def sort_bombelkowe(tab):
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

def wyciaganie_danych(tab):
    granica=tab[1]
    strumien_danych=tab[0]
    count=0
    tab1=([],[])
    for i in range(len(strumien_danych)):
        if count <3:
            if strumien_danych[i] > granica:
                tab1[0].append(i)
                tab1[1].append(strumien_danych[i])
                count=count+1

    return tab1