wiek = 18
if wiek < 18:
    print('małolata')
elif wiek == 18:
    print('pełnoletni')
else:
    print('staruszek')

a = 2
b = 7
a += 1 # a = a+1
print(b**a)

klasa = 'informatycy'
print(klasa[-1])   ## wyswietla ostatnia litere slowa

inf = input()
znak = int(input())
if znak > len(inf):   ## len to funkcja okreslajaca dlugosc slowa (ile ma liter)
    print('ERROR')
else:
    print(inf[znak])   ## zmienna 'znak' okresla jaka literke wypisac

print('Czy liczba jest nieparzysta?')
a = int(input())
if a%2==0:   ## modulo okresla parzystosc czesto
    print('nie')
else:
    print('tak')

for i in range(4):
    print(i)
print('\n')

for i in range(1,4):
    print(i)
print('\n')

for i in range(0,4,2):
    print(i)

## odwracanie liczby ale kazda w osobnej linii
liczba = 12346
while liczba > 0:
    print(liczba%10)
    liczba //=10

licznik = 0
limit = 10
while licznik <= limit:
    print(licznik)
    licznik += 2    # <- ten kod wyswietla liczby od 10 do 0 ale co druga liczbe :3
