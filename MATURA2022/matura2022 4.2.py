plik = open("przyklad.txt")

liczby = []

for linia in plik:
    text = ""
    for litera in linia:
        if litera != "\n":
            text = text + litera
    liczby.append(text)
    


najwiecej_czynnikow = 0
wynik = 0

for i in range(len(liczby)):
    
    liczby[i] = int(liczby[i])
    czynniki = []
    l_czynnikow_roznych = 0
    temp = liczby[i]
    k = 2
    
    
    while liczby[i] != 1:
        while liczby[i] % k == 0:

            liczby[i] //= k
            czynniki.append(k)

            if len(czynniki) > najwiecej_czynnikow:
                najwiecej_czynnikow = len(czynniki)
                maks = temp
                
            if czynniki.count(k) == 1:
                l_czynnikow_roznych += 1
                if wynik < l_czynnikow_roznych:
                    wynik = l_czynnikow_roznych
                    rozne = temp

        k += 1
    liczby[i] = temp
    print(liczby[i], czynniki)

print(" ")
print(maks, najwiecej_czynnikow)
print(rozne, wynik)
