plik = open("przyklad.txt")
wpisywanie_trojek = open("trojki.txt", "w")
wpisywanie_piatek = open("piatki.txt", "w")
linie = plik.readlines()
trojka = 0
piatka = 0
wpis = []
for i in range(len(linie)):
    linie[i] = linie[i].strip("\n")

for i in range(len(linie)):
    for j in range(1,len(linie)):
        for k in range(2,len(linie)):
            linie[i] = int(linie[i])
            linie[j] = int(linie[j])
            linie[k] = int(linie[k])
            if linie[i] != 0 and linie[j] != 0 and linie[k] != 0 and linie[i] != linie[j] and linie[j] != linie[k]:
                if linie[j] % linie[i] == 0 and linie[k] % linie[j] == 0:
                    trojka += 1
                    linie[i] = str(linie[i])
                    linie[j] = str(linie[j])
                    linie[k] = str(linie[k])
                    wpisywanie_trojek.write(linie[i])
                    wpisywanie_trojek.write(" ")
                    wpisywanie_trojek.write(linie[j])
                    wpisywanie_trojek.write(" ")
                    wpisywanie_trojek.write(linie[k])
                    wpisywanie_trojek.write("\n")
               
print(trojka)
print(piatka)
