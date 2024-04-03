## wiadomosc 150

napis = input()
dlugosc = len(napis)
if dlugosc <=150:
    print(napis)
    print('idealna długość napisu')
else:
    ## wyswietlanie pierwszych 150 znakow
    print(napis[:150])
    print('za długi napis')

### tablice
lista = []
lista = [1,2,5,2,5]
lista_prezentow = ['zabawki', 'slodycze', 'gra']
print(lista_prezentow[0])
print(lista_prezentow)

for i in lista_prezentow:
    print(i)

for i in range(len(lista_prezentow)):
    print(lista_prezentow[i])

lista_prezentow.append('pieniądze')
print(lista_prezentow)

## liczby parzyste w tablicy 10-100 włącznie
tab_parzyste = []
for liczba in range(10,101):
    if liczba%2 == 0:
        tab_parzyste.append(liczba)
print(tab_parzyste)

## liczby podzielne przez 3 trzycyfrowe w tablicy zapisać
tab_podzielne = []
for i in range(100,1000):
    if i%3 == 0:
        tab_podzielne.append(i)
print(tab_podzielne)

## wypisać dzielniki liczby
liczba = int(input())
tab_dzielniki = []
for i in range(1, liczba + 1):
    if liczba%i == 0:
        tab_dzielniki.append(i)
print(tab_dzielniki)
