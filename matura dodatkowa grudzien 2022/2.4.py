

plik = open("pary.txt")

para = list(map(str.split, plik))



def rysuj(x, y):
    n = 100000
    if 2 * x <= n:
        if y == 2*x:
            print("strzałka", x, 2 * x)

        rysuj(2 * x, y)
    if 2 * x + 1 <= n:
        if y == 2 * x + 1:
            print("strzałka", x, 2 * x + 1)
        rysuj(2 * x + 1, y)

for i in range(len(para)):
    rysuj(int(para[i][0]), int(para[i][1]))