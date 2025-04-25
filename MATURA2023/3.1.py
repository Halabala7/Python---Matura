plik = open("pi.txt")

linie = plik.readlines()
for i in range(len(linie)):
    linie[i] = linie[i].rstrip()

fragment = []

for i in range(len(linie)-1):
    fragment.append(linie[i] + linie[i+1])

licznik = 0
for i in range(len(fragment)):
    if int(fragment[i]) > 90:
        licznik += 1

print(licznik)
