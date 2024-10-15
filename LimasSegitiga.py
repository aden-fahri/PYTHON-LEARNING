print('='*60)
print('menghitung volume, luas permukaan limas segitiga')
print('='*60)
def LimasSegitiga():
    l = int(input('masukkan nilai luas alas limas segitiga\t: '))
    t = int(input('masukkan tinggi limas segitiga\t\t: '))
    luas_sisi_tegak_1 = int(input('masukkan nilai luas sisi tegak 1\t: '))
    luas_sisi_tegak_2 = int(input('masukkan nilai luas tegak 2\t\t: '))
    luas_sisi_tegak_3 = int(input('masukkan nilai luas tegak 3\t\t: '))

    v = lambda l, t, luas_sisi_tegak_1, luas_sisi_tegak_2, luas_sisi_tegak_3: 1/3 * l * t
    luas_permukaan = lambda l, t, luas_sisi_tegak_1, luas_sisi_tegak_2, luas_sisi_tegak_3: l + luas_sisi_tegak_1 + luas_sisi_tegak_2 + luas_sisi_tegak_3
    print('- '*20)
    print('nilai volume limas segitiga adalah\t: ',v(l, t, luas_sisi_tegak_1, luas_sisi_tegak_2, luas_sisi_tegak_3))
    print('nilai luas permukaan limas segitiga adalah: ',luas_permukaan(l, t, luas_sisi_tegak_1, luas_sisi_tegak_2, luas_sisi_tegak_3))
LimasSegitiga()
print('- '*30)
LimasSegitiga()