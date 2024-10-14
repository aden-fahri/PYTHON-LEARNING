print('='*60)
print('menghitung volume, luas, dan keliling balok')
print('='*60)

def balok():
    p = int(input('masukkan panjang balok: '))
    l = int(input('masukkan lebar balok: '))
    t = int(input('masukkan tinggi balok: '))

    volume =lambda p, l, t: p * l * t
    luas = lambda p, l, t: 2*(p * l) + (p * t) + (l * t)
    keliling = lambda p, l, r: 4*(p + l + t)

    print('nilai volume balok adalah: ', volume(p, l, t))
    print('nilai luas balok adalah: ', luas(p, l, t))
    print('nilai keliling balok adalah: ', keliling(p, l, t))

balok()
print('- '*20)
balok()