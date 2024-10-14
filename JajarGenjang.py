print('='*40)
print(' luas dan keliling jajar genjang ')
print('='*40)

def JajarGenjang():
    alas = int(input('masukkan alas jajar genjang\t\t: '))
    tinggi = int(input('masukkan tinggi jajar genjang\t\t: '))
    panjang_sisi_jajar_genjang_a = float(input('masukan panjang_sisi_jajar_genjang_a\t: '))
    panjang_sisi_jajar_genjang_b = float(input('masukkan panjang_sisi_jajar_genjang_b\t: '))

    luas = lambda alas, tinggi, panjang_sisi_jajar_genjang_a, panjang_sisi_jajar_genjang_b:   alas * tinggi
    keliling = lambda alas, tinggi, panjang_sisi_jajar_genjang_a, panjang_sisi_jajar_genjang_b: 2 * (panjang_sisi_jajar_genjang_a + panjang_sisi_jajar_genjang_b)
    print(f'hasil luas jajar genjang adalah\t\t: ', luas(alas, tinggi, panjang_sisi_jajar_genjang_a, panjang_sisi_jajar_genjang_b))
    print(f'hasil keliling jajar genjang adalah\t: ', keliling(alas, tinggi, panjang_sisi_jajar_genjang_a, panjang_sisi_jajar_genjang_b))
JajarGenjang()
print('- '*20)
JajarGenjang()