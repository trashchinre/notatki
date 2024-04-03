# 1 ## Użytkownik podaje nazwisko a program skraca je do 20 znaków
nazwisko = input()
if len(nazwisko) > 20:
    skr_nazwisko = nazwisko[:20]
    print(f"Skrócone nazwisko: {skr_nazwisko}")


# 2 ## użytkownik podaje oceny po spacji i program zapisuje w tablicy oblicza mu średnią, max i min wartość. 
#####  Dla danych 1 2 3 średnia 2 min 1 max 3
oceny = list(map(int, input().split()))
srednia = sum(oceny) / len(oceny)
max_ocena = max(oceny)
min_ocena = min(oceny)
print(f"Średnia ocen: {srednia}")
print(f"Minimalna ocena: {min_ocena}")
print(f"Maksymalna ocena: {max_ocena}")


# 3 ## Użytkownik podaje liczbę od 0 do 10 i program wypisuje mu wszystkie liczby od 0 do 100 oprócz wybranej i ich 
#####  wielokrotności  - - -  Dla danych 3  -  0 1 2 4 5 7 8 10….
wybrana_liczba = int(input("Podaj liczbę od 0 do 10: "))
for liczba in range(101):
    if liczba != wybrana_liczba and liczba % wybrana_liczba != 0:
        print(liczba, end=" ")


# 4 ## Użytkownik podaje liczbę, a program liczy mu liczbę binarną. Program działa w pętli za każdym razem pytając się 
#####  czy to już koniec
k = "nie"
while k == "nie":
    liczba = int(input())
    liczba_bin = bin(liczba)[2:]
    print(f"Liczba binarna dla {liczba} to {liczba_bin}")
    k = input("to juz koniec? ")


# 5 ## Program sprawdzający czy słowo jest palindromem
slowo = input()
if slowo == slowo[::-1]:
    print(f"{slowo} to palindrom")
else:
    print(f"{slowo} to nie palindrom")


# 6 ## Totolotek - losuję 6 liczb od 1 do 49 zapisuję w tablicy. Liczby nie mogą się powtarzać
import random
def losuj_lotto():
    return random.sample(range(1, 50), 6)
wylosowane = losuj_lotto()
print("Wylosowane liczby to:", wylosowane)

# 7 ## Drukuje lata przestępne od 1800 - przestępne to takie, gdzie liczba jest podzielna przez 4 i niepodzielna przez 100
#####  lub jest podzielna przez 400. Dotychczas według tej reguły lata 1600 i 2000 były przestępnymi, a lata 1700, 1800, 
#####  1900 nie. W przyszłości rok 2100 nie będzie rokiem przestępnym
# # # # Zadanie przy pomocy AI.
def czy_przestepny(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
        return True
    else:
        return False
def drukuj_przestepne(od_roku, do_roku):
    print("Lata przestępne od", od_roku, "do", do_roku, ":")
    for rok in range(od_roku, do_roku + 1):
        if czy_przestepny(rok):
            print(rok)
drukuj_przestepne(1800, 2100)
