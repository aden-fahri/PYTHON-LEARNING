print('='*30)
print('luas dan keliling persegi panjang')
print('='*30)

def persegi_panjang():
    panjang = int(input('masukkan panjang persegi panjang\t: '))
    lebar = int(input('masukkan lebar persegi panjang\t\t: '))

    luas = lambda panjang, lebar: panjang * lebar
    keliling =lambda panjang, lebar: 2 * (panjang + lebar)

    print('luas persegi panjang adalah\t\t: ', luas(panjang, lebar))
    print('keliling persegi panjang adalah\t\t: ', keliling(panjang, lebar))

persegi_panjang()
print('- '*15)
persegi_panjang()
print('- '*15)