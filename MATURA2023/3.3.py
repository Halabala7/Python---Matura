plik = open("pi.txt")

linie = plik.readlines()
for i in range(len(linie)):
    linie[i] = linie[i].rstrip()


text = "".join(linie)
licznik = 0


for i in range(len(text)-5):

    if text[i] < text[i+1] and text[i+1] > text[i+2] > text[i+3] > text[i+4] > text[i+5]:
        licznik += 1
    elif text[i] < text[i+1] <= text[i+2] and text[i+2] > text[i+3] > text[i+4] > text[i+5]:
        licznik += 1
    elif text[i] < text[i+1] <= text[i+2] <= text[i+3] and text[i+3] > text[i+4] > text[i+5]:
        licznik += 1
print(licznik)
