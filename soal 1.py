import random

list_angka = []

for i in random.sample(range(1, 100), 10):
    list_angka.append(i)
print(list_angka)

sep = int(input('pemisah:'))

def pemisah(list_angka, sep):
    sum = 0
    for i in range (len(list_angka)):
        if list_angka[i] % sep == 0:
            sum += list_angka[i]
        else:
            continue
    return f'jumlah = {sum}'

print(pemisah(list_angka, sep))
