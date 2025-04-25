plik = open("instrukcje.txt")
Litery = []
Rozkazy = []
text = ""

for linia in plik:

    for litera in linia:
        if litera == " ":
            break
        else:
            text = text + litera
    if text == "DOPISZ":
        dlugosc = len(linia)-2
        Litery.append(linia[dlugosc])
        Rozkazy.append(text)
    text = ""
znak = Litery[0]
wynik = Litery.count(znak)
for i in range(len(Litery)):
    if Litery.count(Litery[i]) > wynik:
        wynik = Litery.count(Litery[i])
        znak = Litery[i]

print(wynik, znak)
