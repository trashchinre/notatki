liczba = 23
liczba_binarna = bin(liczba)
print(liczba_binarna[2:])

while True:
    if input().lower() == 'exit':
        break

# zad ## Gierka - komputer losuje liczby od 1 do 10 a użytkownik ma zgadnąć jaka liczba została wylosowana - za każdym 
#####    razem użytkownik się dowiaduje czy ma podać liczbę większą czy mniejszą
import random
bot = random.randint(1,11)
print(bot)
