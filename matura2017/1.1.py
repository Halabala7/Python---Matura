A = [7, 5, 11, 33]
p = 3
wynik = []
for i in range(len(A)):
    for j in range(len(A)):
        if A[i] != A[j]:
            pole = A[i] * A[j]
            if pole % p == 0:
                continue
            else:
                wynik.append(pole)


if wynik == []:
    print(0)
else:
    S = wynik[0]
    for i in range(len(wynik)):
        if naj < wynik[i]:
            naj = wynik[i]
    print(S)
