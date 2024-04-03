def czy_ulamek():
    #wczytuje
    a,b = map(int, input().split())
    #czy w przedziale
    if -1024 <= a <= 1024 and -1024 <= b <= 1024:
        #czy ich iloraz posiada czesc ulamkowa
        if a%b != 0:
            print('tak')
        else:
            print('nie')

    else:
        print('Liczby poza przedziałem')

#pobieram napis i wyswietlam w odwrotnej kolejnosci
a = input()
print(a[::-1])
if a == a[::-1]:
    print('palindrom')
else:
    print('nie palindrom')

# petla while
a=5
while a > 0:
    print(a)
    a -= 1
