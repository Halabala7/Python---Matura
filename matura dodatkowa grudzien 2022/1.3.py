file = open("mecz.txt")
counter = 0
old_counter = 0
win = 0
letter = ""
for line in file:
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            counter += 1
        else:
            if counter >= 10:
                win += 1
                counter += 1
                if old_counter < counter:
                    old_counter = counter
                    letter = line[i]
            counter = 0
print(win, letter, old_counter)
