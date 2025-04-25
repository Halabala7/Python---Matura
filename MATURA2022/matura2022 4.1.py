plik = open("przyklad.txt")

text = ""
tab = []
licznik = 0
for linia in plik:

    if linia[0] == linia[(len(linia))-2]:

        for literka in linia:

            if literka != "\n":

                text = text + literka

        tab.append(text)
        text = ""

print(len(tab), tab[0])
