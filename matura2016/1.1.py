from itertools import chain

plik = open("punkty.txt")
text = ""
liczby = []
linie = plik.readlines()


linie = list(map(str.rstrip, linie))
linie = list(map(str.split, linie))
linie = list(chain.from_iterable(linie))

print(linie)
for i in range()
    for j in range()