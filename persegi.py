print('='*30)
print('      luas persegi    ')
print('='*30)

def persegi():
    sisi = int(input('masukan nilai sisi\t: '))
    luas = lambda s: sisi * sisi
    keliling = lambda s: 4 * sisi

    print('luas persegi\t\t:',luas(luas),'cm2')
    print('keliling persegi\t:',keliling(keliling), 'cm')

persegi()
print('- '*15)
persegi()
print('- '*15)
persegi()