def rysuj(x):
    n=
    if 2*x <= n:
        print("strzałka", x, 2*x)
        rysuj(2*x)
    if 2*x +1 <= n:
        print("strzałka", x, 2*x + 1)
        rysuj(2*x + 1)

rysuj(1)

