import matplotlib.pyplot as plt
import math

file = open("punkty.txt")
line = file.readlines()

line = list(map(str.split, line))

x = []
y = []
for i in range(len(line)):
    x.append(line[i][0])
    y.append(line[i][1])

line.clear()

x = list(map(int, x))
y = list(map(int, y))

calc_pi = []
for n in range(1, 1701):
    counter = 0
    for i in range(n):
        if (x[i]-200)**2 + (y[i]-200)**2 <= 200**2:
            counter += 1
    wynik = (4*counter)/n
    if n == 1000 or n == 1700:
        wynik = wynik-math.pi
        wynik = wynik.__round__(4)
        print("pi", n, wynik)
    else:
        wynik = wynik-math.pi
        wynik = wynik.__round__(4)
    if wynik < 0:
        wynik = wynik * -1
    calc_pi.append(wynik)


plt.figure(figsize=(10, 5))
plt.plot(calc_pi)
plt.title("zmiana wygladu ok")
plt.show()
