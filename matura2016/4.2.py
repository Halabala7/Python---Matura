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


counter = 0
for i in range(1000):
    if (x[i]-200)**2 + (y[i]-200)**2 <= 200**2:
        counter += 1
wynik = (4*counter)/1000
wynik = wynik.__round__(4)
print("pi 1000", wynik)

counter = 0
for i in range(5000):
    if (x[i]-200)**2 + (y[i]-200)**2 <= 200**2:
        counter += 1
wynik = (4*counter)/5000
wynik = wynik.__round__(4)
print("pi 5000", wynik)

counter = 0
for i in range(len(x)):
    if (x[i]-200)**2 + (y[i]-200)**2 <= 200**2:
        counter += 1
wynik = (4*counter)/10000
wynik = wynik.__round__(4)
print("pi z wszystkich", wynik)
