print('='*30)
print('pengulangan 5')
print('='*30)

jumlah = 0
for x in range(1, 6):
    if x < 5:
        print(x, end= ' + ')
    else:
        print(x, end= ' = ')
    jumlah = jumlah + (x)
print(jumlah)