# liczby losowe
import random
a=int(input('Podaj liczbe: '))
licznik=0
suma=0
for i in range(a):
    liczba_losowa=random.randint(-10,10)
    if liczba_losowa>0:
        licznik+=1
        suma+=liczba_losowa
        print(f'Wieksza od zera: {liczba_losowa}')
print(f'Liczb wiekszych od zera bylo {licznik}')
print(f'Liczb mniejszych lub rownych zera bylo {a-licznik}')
print(suma)

import random
for i in range(6):
    print(random.randint(1,49))

# jakies cool funkcje
imie = 'janek'
print(imie[0])
print(imie[-1])
print(imie.upper())
print(imie[::2])
print(imie.title())
print(imie.lower())
print(imie[::-1])

ok = 'kajak'
if (ok == ok[::-1]):
    print(True)
else:
    print(False)
# krocej
print(True if ok == ok[::-1] else False)

word1 = 'burza'
word2 = 'arbuz'
word3 = 'adama'

if sorted(word1) == sorted(word2):
    print('anagram')
else: print('nie anagram')

a = int(input('Podaj liczbe owocow: '))
licznik = 0
lista = []
while licznik < a:
    owoc = input('Podaj owoc: ')
    lista.append(owoc)
    licznik += 1
print(lista)

# kamien papier nozyce - tabelki
import random
p1 = input('Wybierz opcje: k / p / n \n').lower()

options = ['k', 'p', 'n']
p2 = random.choice(options)
if p1 in options:
    print(p2)
    if p1 == p2:
        print('remis')
    elif p1 == 'n' and p2 == 'p' or p1 == 'k' and p2 == 'n' or p1 == 'p' and p2 == 'k':
        print('win player 1')
    else:
        print('win player 2')
else:
    print('nieprawidlowa opcja')
