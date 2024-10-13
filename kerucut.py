print('='*30)
print('volume, luas permukaan, dan luas selimut kerucut')
print('='*30)

PHI = 3.14
r = float(input('masukkan jari jari kerucut: '))
t = float(input('masukkan tinggi kerucut: '))
s = float(input('masukkan jarak dari puncak kerucut ke tepi alas: '))

v = (1/3) * PHI * r**2 * t
a = PHI * r * (r * s)
ls = PHI * r * s

print(f'nilai volume kerucut adalah: ', v)
print(f'nilai luas permuakaan kerucut adalah: ', a)
print(f'nilai luas selimut kerucut adalah: ', ls)