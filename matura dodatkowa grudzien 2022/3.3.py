file = open("liczby_przyklad.txt")
numbers = list(map(str.rstrip, file))
numbers = list(map(int, numbers))

max = max(numbers)
first = [2]


for j in range(3, max+1, 2):
     k = 2
     counter = 0
     while j >= k:
         if j % k == 0:
             counter += 1
             if counter > 1:
                 break
         k += 1
     if counter == 1:
         first.append(j)

max_number = 0
min_number = 0
max_counter_in_memory = 0
min_counter_in_memory = 0

used = []
backup_first = first.copy()
for number in numbers:
    counter = 0
    first = backup_first.copy()
    i = 0
    while i < len(first):
        j = 1
        while j < len(first):
            if number == first[i] + first[j]:
                used.a

                counter += 1
                if counter >= max_counter_in_memory:
                    max_counter_in_memory = counter
                    max_number = number
            j+=1
        i+=1


print(max_number, max_counter_in_memory)

file.close()
