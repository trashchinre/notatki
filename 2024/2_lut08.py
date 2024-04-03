import random
a=int(input('Ile razy chcesz losowac czy orzel czy reszka?  '))
licznik_orlow = 0
licznik_reszek = 0
for i in range(a):
    los = random.randint(0,1)
    print(f'\n{i+1} losowanie:')
    if los == 0:
        print('orzel')
        licznik_orlow+=1
    else:
        print('reszka')
        licznik_reszek+=1
print(f'\n {licznik_orlow} - orlow \n {licznik_reszek} - reszek')

liczba_ocen = int(input('Podaj liczbe ocen: '))
suma = 0
for i in range(liczba_ocen):
    oceny = float(input('Jaka ocene dostales? - '))
    suma += oceny

print(suma/liczba_ocen)
