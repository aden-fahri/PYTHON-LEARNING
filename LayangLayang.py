print('='*60)
print('menghitung luas layang layang')
print('='*60)

def LayangLayang():
    d1 = int(input('masukkan diagonal 1 layang layang: '))
    d2 = int(input('masukkan diagonal 2 layang layang: '))

    luas = lambda d1, d2: 1/2 * d1 * d2

    print('luas layang layang adalah:', luas(d1, d2))
LayangLayang()
print(' -'*15)
LayangLayang()