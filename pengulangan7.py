print('='*30)
print('pengulangan 7')
print('='*30)

jumlah = 0
for x in range(1, 6, 2):
    if x < 4:
        print(x, end= ' + ')
    else:
        print(x, end= ' = ')
    jumlah = jumlah + (x)
print(jumlah)