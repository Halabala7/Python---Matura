def przedstaw(A):

    klucz = A[0]
    w = 0
    licznik = 0
    for k in range(2, len(A)):
        if A[k] < klucz:
            licznik += 1
            temp = A[w]
            A[w] = A[k]
            A[k] = temp
            w = w+1
    print(A)
    print(w+1)


A = []
for n in range(10, 0, -1):
    for i in range(n, 101, 10):
        A.append(i)

przedstaw(A)
