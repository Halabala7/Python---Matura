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

print("punkty nalezace do brzegu kola: ")
counter = 0
counter_inside = 0
for i in range(len(x)):
    if (x[i]-200)**2 + (y[i]-200)**2 == 200**2:
        counter += 1
        print(x[i], y[i])


print("ilosc punktow: ", counter)

counter = 0
print("punkty nalezace do wnetrza kola: ")
for i in range(len(x)):
    if (x[i]-200)**2 + (y[i]-200)**2 < 200**2:
        counter += 1


print("ilosc punktow: ", counter)
