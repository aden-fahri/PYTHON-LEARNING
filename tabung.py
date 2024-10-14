print('='*40)
print('menghitung volume, luas, keliling')
print('='*40)

def tabung():
    PHI = 3.14
    r = int(input('masukkan nilai jari jari tabung\t: '))
    t = int(input('masukkan nilai tinggi tabung\t: '))

    volume = lambda PHI, r, t: PHI * r**2 * t
    luas = lambda PHI, r, t: 2 * PHI * r * (r + t)
    keliling = lambda PHI, r, t: 2 * PHI * r
    print('- '*30)
    print('nilai volume tabung adalah\t: ',volume(PHI, r, t))
    print('nilai luas tabung adalah\t: ',luas(PHI, r, t))
    print('nilai keliling tabung adalah\t: ',keliling(PHI, r, t))
tabung()
print('- '*30)
tabung()