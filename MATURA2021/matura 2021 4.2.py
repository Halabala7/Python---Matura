plik = open("instrukcje.txt")
tablica = []
text = ""
for linia in plik:
    for litera in linia:
        if litera == " ":
            break
        else:
            text = text + litera
    tablica.append(text)
    text = ""

licznik = 0
j = 1
wynik = 0
for i in range(len(tablica)):
    if j < len(tablica):
        if (tablica[i] == tablica[j]):

            licznik += 1

            if licznik > wynik:
                wynik = licznik
                index = tablica[i]
        else:
            licznik = 0
        j += 1
print(wynik+1, index)
