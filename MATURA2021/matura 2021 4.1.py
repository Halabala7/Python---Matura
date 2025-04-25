Litery = []
Rozkazy = []
Neon = []
plik = open("przyklad.txt")


text = ""

for linia in plik:
    dlugosc = len(linia)-2
    Litery.append(linia[dlugosc])
    for litera in linia:
        if litera == " ":
            break
        else:
            text = text + litera
    Rozkazy.append(text)
    text = ""
for i in range(len(Rozkazy)):
    if Rozkazy[i] == "DOPISZ":
        Neon.append(Litery[i])
    elif Rozkazy[i] == "USUN":
        Neon.pop()
    elif Rozkazy[i] == "ZMIEN":
        Neon.pop()
        Neon.append(Litery[i])
    elif Rozkazy[i] == "PRZESUN":
        for j in range(len(Neon)):
            if Neon[j] == Litery[i]:
                if Neon[j] == "Z":
                    Neon[j] = "A"
                else:
                    Neon[j] = ord(Neon[j])
                    Neon[j] = chr(Neon[j] + 1)

print(len(Neon))
