plik = open("dane.txt")
tablica_dwuwymiarowa = []
text = ""

for linia in plik:
    wiersz = [int(liczba_str) for liczba_str in linia.split()]
    tablica_dwuwymiarowa.append(wiersz)
licznik = 0
najdluzszy = 0
for j in range(320):
    for i in range(199):
        if tablica_dwuwymiarowa[i][j] == tablica_dwuwymiarowa[i+1][j]:
            licznik += 1
        else:
            licznik = 0
        if najdluzszy <= licznik:
            najdluzszy = licznik

print(najdluzszy+1)
