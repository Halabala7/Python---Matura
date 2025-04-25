plik = open("dane.txt")
liczby = []
text = ""

for linia in plik:
    for litera in linia.split():
        liczby.append(litera)
liczby = list(map(int, liczby))
print(max(liczby))
print(min(liczby))
