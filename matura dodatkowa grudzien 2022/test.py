tab = [1,2,3,4,5,6]
for i in range(len(tab)):
    if tab.count(2) == 1:
        index = tab.index(2)
        tab.__delitem__(index)
    print(tab[i])