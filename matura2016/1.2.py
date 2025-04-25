n = 20
suma = 0
for i in range(1, n):
    if n % i == 0:
        suma = suma + i
nowasuma = 0
suma -= 1
print(suma)
for i in range(1, suma):
    if suma % i == 0:
        nowasuma = nowasuma + i
nowasuma -= 1
print(nowasuma)
if nowasuma == n:
    print("TAK")
else:
    print("NIE")
