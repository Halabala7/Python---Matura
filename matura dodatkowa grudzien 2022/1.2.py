file = open("mecz.txt")
counterA = 0
counterB = 0
for line in file:
    for i in range(len(line)):
        if line[i] == "A":
            counterA += 1
            if counterA >= 1000:
                if counterA - counterB >= 3:
                    print("A", counterA, counterB)
                    break
        elif line[i] == "B":
            counterB += 1
            if counterB >= 1000:
                if counterB - counterA >= 3:
                    print("B", counterB, counterA)
                    break
        else:
            continue


file.close()