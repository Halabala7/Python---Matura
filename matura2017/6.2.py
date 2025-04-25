plik = open("dane.txt")
tablica_dwuwymiarowa = []
text = ""

for linia in plik:
    wiersz = [int(liczba_str) for liczba_str in linia.split()]
    tablica_dwuwymiarowa.append(wiersz)
counter = 0
for i in range(200):
    for j in range(320):
        if int(tablica_dwuwymiarowa[i][j]) != int(tablica_dwuwymiarowa[i][319-j]):
            counter += 1
            break
print(counter)
