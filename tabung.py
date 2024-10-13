print('='*30)
print('menghitung volume, luas, keliling')
print('='*30)

PHI = 3.14
r = int(input('masukkan nilai jari jari tabung\t: '))
t = int(input('masukkan nilai tinggi tabung\t: '))

volume = PHI * r**2 * t
luas = 2 * PHI * r * (r + t)
keliling = 2 * PHI * r
print('- '*30)
print('nilai volume tabung adalah\t: ',volume)
print('nilai luas tabung adalah\t: ',luas)
print('nilai keliling tabung adalah\t: ',keliling)