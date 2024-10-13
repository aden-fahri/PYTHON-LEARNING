print('='*30)
print(' trapesium ')
print('='*30)

tinggi = int(input('masukkan nilai tinggi trapesium: '))
sisi_sejajar_a = int(input('masukkan nilai sisi sejajar a: '))
sisi_sejajar_b= int(input('masukkan nilai sisi sejajar b: '))

luas = 1/2 * (sisi_sejajar_a + sisi_sejajar_b) * tinggi
print(f'nilai trapesium adalah: ', luas)