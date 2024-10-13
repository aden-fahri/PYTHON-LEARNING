print('='*30)
print(' luas dan keliling jajar genjang ')
print('='*30)

alas = float(input('masukkan alas jajar genjang: '))
tinggi = float(input('masukkan tinggi jajar genjang: '))
panjang_sisi_jajar_genjang_a = float(input('masukan panjang_sisi_jajar_genjang_a: '))
panjang_sisi_jajar_genjang_b = float(input('masukkan panjang_sisi_jajar_genjang_b: '))

luas = alas * tinggi
keliling = 2 * (panjang_sisi_jajar_genjang_a + panjang_sisi_jajar_genjang_b)
print(f'hasil luas jajar genjang adalah: ', luas)
print(f'hasil keliling jajar genjang adalah: ', keliling)