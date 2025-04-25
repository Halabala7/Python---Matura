file = open("mecz.txt")
counter = 0
for line in file:
    for i in range(len(line)-1):
        if line[i] != line[i+1]:
            counter+=1
        else:
            continue
print(counter)