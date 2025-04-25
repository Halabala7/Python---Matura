plik = open("bin_przyklad.txt")

linie = plik.readlines()
for i in range(len(linie)):
    linie[i] = linie[i].strip("\n")
linie = list(set(linie))
wynik = []
for i in range(len(linie)):
    znak = linie[i][0]

    blok = 0
    for j in range(len(linie[i])):
        if linie[i][j] == znak:
            continue
        else:
            if blok <= 2:
                znak = linie[i][j]
                blok += 1
            elif blok > 2:
                wynik.append(linie[i])

print(wynik)
