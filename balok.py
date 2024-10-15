print('='*60)
print('menghitung volume, luas, dan keliling balok')
print('='*60)

def balok():
    p = int(input('masukkan panjang balok\t: '))
    l = int(input('masukkan lebar balok\t: '))
    t = int(input('masukkan tinggi balok\t: '))

    volume =lambda p, l, t: p * l * t
    luas = lambda p, l, t: 2*(p * l) + (p * t) + (l * t)
    keliling = lambda p, l, r: 4*(p + l + t)

    print('_ '*25)
    print('nilai volume balok adalah\t: ', volume(p, l, t))
    print('nilai luas balok adalah\t\t: ', luas(p, l, t))
    print('nilai keliling balok adalah\t: ', keliling(p, l, t))

balok()
print('- '*25)
balok()