plik = open("pi.txt")

linie = plik.readlines()
for i in range(len(linie)):
    linie[i] = linie[i].rstrip()

fragment = []

for i in range(len(linie)-1):
    fragment.append(linie[i] + linie[i+1])

sprawdzanie_fragmentow = []
for i in range(0, 100):
    i = str(i)
    if len(i) == 1:
        i = "0"+i
    sprawdzanie_fragmentow.append(i)


min_wystapien = fragment.count(sprawdzanie_fragmentow[0])
liczba_min_wystapien = 0
max_wystapien = fragment.count(sprawdzanie_fragmentow[0])
liczba_max_wystapien = 0

for i in range(len(sprawdzanie_fragmentow)):
    if min_wystapien > fragment.count(sprawdzanie_fragmentow[i]):
        min_wystapien = fragment.count(sprawdzanie_fragmentow[i])
        liczba_min_wystapien = sprawdzanie_fragmentow[i]
    if max_wystapien < fragment.count(sprawdzanie_fragmentow[i]):
        max_wystapien = fragment.count(sprawdzanie_fragmentow[i])
        liczba_max_wystapien = sprawdzanie_fragmentow[i]


print(min_wystapien, liczba_min_wystapien)
print(max_wystapien, liczba_max_wystapien)
