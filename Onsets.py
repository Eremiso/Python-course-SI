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

def wyciaganie_indeks_bombelkowo(tab):
    granica=tab[1]
    strumien_danych=tab[0]
    count=0
    dane=[]
    for i in range(len(strumien_danych)):
        if count <3:
            if strumien_danych[i] > granica:
                z=[]
                z.append(strumien_danych[i])
                z.append(i)
                dane.append(z)
                count=count+1
    zz=sort_bombelkowe(dane)
    zz.reverse()
    wynik=[]
    for i in range(3):
        wynik.append(zz[i][1])
    return wynik

def wyciaganie_indeks_wstawianie(tab):
    granica=tab[1]
    strumien_danych=tab[0]
    count=0
    dane=[]
    for i in range(len(strumien_danych)):
        if count <3:
            if strumien_danych[i] > granica:
                z=[]
                z.append(strumien_danych[i])
                z.append(i)
                dane.append(z)
                count=count+1
    zz=sort_wstawianie(dane)
    zz.reverse()
    wynik=[]
    for i in range(3):
        wynik.append(zz[i][1])
    return wynik



lista_1 = ([11,2,6,1,1,1,1,0,2,3,4,10,11],3)
print(wyciaganie_indeks_bombelkowo(lista_1))
print(wyciaganie_indeks_wstawianie(lista_1))