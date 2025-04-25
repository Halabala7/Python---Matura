file = open("liczby.txt")
numbers = list(map(str.rstrip, file))
numbers = list(map(int, numbers))
sum = 0


for i in range(len(numbers)):
    numbers[i] -= 1
    j = 1
    counter = 0
    while j <= numbers[i]:

        if numbers[i] % j == 0:
            counter += 1
        j += 1
    if counter <= 2:
        sum += 1



print("pierwsze")
print(sum)
