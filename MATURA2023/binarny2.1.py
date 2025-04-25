n = 67

potegi_dwojki = [1]

i = 0
while potegi_dwojki[i] < n:
    i += 1
    potega = 2**i
    potegi_dwojki.append(potega)
liczby_do_zamiany = []
binarna = ""
potegi_dwojki.reverse()
for i in range(len(potegi_dwojki)):
    if potegi_dwojki[i] > n:
        binarna += "0"

    else:
        liczby_do_zamiany.append(potegi_dwojki[i])
        n = n-potegi_dwojki[i]
        binarna += "1"

znak = binarna[0]
blok = 0
for i in range(len(binarna)):
    if binarna[i] == znak:
        continue
    else:
        blok += 1

print(binarna, blok)
