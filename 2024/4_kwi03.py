# while True: #pętla nieskończona
#     print("OK")

# counter = 0
# limit = 10
# while counter <= limit:
#     print(counter, end=" ")
#     counter += 1


########### KARTA PRACY

# Zadanie 1
print("Wpisz liczbe a:")
input_a = int(input())
if input_a%3==0:
    print("Tak")
else:
    print("Nie")

# Zadanie 2
print("Wpisz liczbe a:")
input_a = int(input())
if 100 <= input_a  >= 999 & input_a%17==0 :
    print("Tak")
else:
    print("Nie")

# Zadanie 3
print("Wpisz wiek:")
input_a = int(input())
if input_a<18:
 print("Jesteś niepełnoletni")
else:
 print("Jesteś pełnoletni")

# Zadanie 4
print("Wpisz wage:")
input_a = int(input())
if input_a>20:
 print("Nie możesz wjechać na most")
else:
 print("Możesz bezpiecznie wjechać na most")
 
# Zadanie 5 
# Przykłady:
# 3 6 5 – TAK
# 4 8 9 – NIE
# 3 8 3 – NIE
# 6 3 5 – TAK
print("Wpisz liczbe a:")
input_a = int(input())
print("Wpisz liczbe b:")
input_b = int(input())
print("Wpisz liczbe c:")
input_c = int(input())
if (input_a < input_c and input_b > input_c) or (input_b < input_c and input_a > input_c):
  print("Mieści się")   
else: 
  print("Nie mieści")

# Zadanie 6
print("Podaj dowolną liczbę:")
input_a = int(input())
print("Podaj liczbę pierwszą:")
input_p = int(input())
if (input_a ^ input_p - input_a ) % input_p == 0:
    print("Spełnia")
else:
    print("Nie spełnia")
    
# Zadanie 7
print("Podaj długość skoku:")
input_s = int(input())
print("Podaj punkt startu:")
input_p = int(input())
print("Podaj punkt końcowy:")
input_k = int(input())
if 3*input_s + input_p>= input_k:
    print("Tak")
else:
    print("NIE")
