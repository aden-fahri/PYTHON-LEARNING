print('='*30)
print('menghitung volume, luas, dan keliling balok')
print('='*30)

p = int(input('masukkan panjang balok: '))
l = int(input('masukkan lebar balok: '))
t = int(input('masukkan tinggi balok: '))

volume = p * l * t
luas = 2*(p * l + p * t + l * t)
keliling = 4*(p + l + t)

print('nilai volume balok adalah: ', volume)
print('nilai luas balok adalah: ', luas)
print('nilai keliling balok adalah: ', keliling)