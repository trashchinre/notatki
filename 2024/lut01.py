# dzielniki liczby
licznik = 1
liczba = int(input())

# if warunek:
#   robimi
# elif jakis inny warunek
# else: jesli zaden z warunkow to wtedy sie wykonuje

# wyznaczanie dzielnikow liczby
while licznik <= liczba: # jesli warunek spelniony
    if liczba % licznik ==0:
        print(licznik)
    licznik += 1

a, b = 10, 12
while b != 0:
    a, b = b, a%b
    
liczba = 10
licznik = 2 # wczesniej 0
while licznik < liczba: # wczesniej zamiast < bylo <=
    print(licznik)
    licznik += 2

for i in range(2,10,2):
    print(i) # to samo co wczesniej

# zad 11 - Jestes sedzia zawodow, wlasnie odliczasz czas od 10 do 1. Wyswietl te liczby na ekranie
# za kazdym razem z odpowiednia liczba kropek

for i in range(10,0,-1): # -1 odpowiada za to, by lecialo w druga strone - od 10 do 1 (czyli 0)
    print(i*'.')
# to samo, w petli while 
l=10
while l>0:
    print(l*'.')
    l-=1

# tablice
pisak = 7
pisak = [7,8,9,4,3,2]
