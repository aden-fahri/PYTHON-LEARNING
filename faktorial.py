print('=' * 50)
print('\tMenghitung Faktorial')
print('=' * 50)

angka = int(input('Masukkan angka: '))

faktorial = 1
for x in range(1, angka + 1):
    faktorial *= x

print('Faktorial dari',angka,'adalah',faktorial)
