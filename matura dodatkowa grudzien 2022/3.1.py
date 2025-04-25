n = 50
sito = []

sito.append("Fałsz")
for i in range(1, n):
    sito[i] = "Prawda"
for i in range(1, n):
    if sito[i] == "Prawda":
        j = 1
        while j <= n:
            sito[j] = sito[i]
            j += 1

