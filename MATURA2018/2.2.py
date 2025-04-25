x = [1, 3, 2, -2]
y = [3, 4, 1, 2]
sorte = []
dlugoscX = 0
najLewoX = 0
najLewoY = 0

for i in x:
    dlugoscX += 1
for i in range(dlugoscX):
    if dlugoscX != 1:
        i = 0
        j = 0
    for j in range(dlugoscX):
        if dlugoscX == 1:
            najLewoX = x[0]
            najLewoY = y[0]
            break

        if (x[i]/y[i]) < (x[j]/y[j]):
            najLewoX = x[i]
            najLewoY = y[i]

        elif (x[i]/y[i]) > (x[j]/y[j]):
            najLewoX = x[j]
            najLewoY = y[j]

    for k in range(0, dlugoscX):

        if x[k] == najLewoX:
            x.pop(k)
            y.pop(k)
            dlugoscX -= 1
            break

    wierzcholki = (najLewoX, najLewoY)
    sorte.append(wierzcholki)


for i in range(0, len(sorte)):
    x.append(sorte[i][0])
    y.append(sorte[i][1])
print(x)
print(y)
