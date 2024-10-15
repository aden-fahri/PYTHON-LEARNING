print('='*30)
print(' trapesium ')
print('='*30)

def trapesium():
    tinggi = int(input('masukkan nilai tinggi trapesium\t: '))
    sisi_sejajar_a = int(input('masukkan nilai sisi sejajar a\t: '))
    sisi_sejajar_b= int(input('masukkan nilai sisi sejajar b\t: '))

    luas = lambda tinggi, sisi_sejajar_a, sisi_sejajar_b:  1/2 * (sisi_sejajar_a + sisi_sejajar_b) * tinggi
    print(f'nilai trapesium adalah\t\t: ', luas(tinggi, sisi_sejajar_a, sisi_sejajar_b))
trapesium()
print('_ '*15)
trapesium()