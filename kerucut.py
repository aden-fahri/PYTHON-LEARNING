print('='*60)
print('volume, luas permukaan, dan luas selimut kerucut')
print('='*60)

def kerucut():
    PHI = 3.14
    r = float(input('masukkan jari jari kerucut\t\t\t: '))
    t = float(input('masukkan tinggi kerucut\t\t\t\t: '))
    s = float(input('masukkan jarak dari puncak kerucut ke tepi alas\t: '))

    v = lambda r, t, s, PHI: (1/3) * PHI * r**2 * t
    a = lambda r, t, s, PHI: PHI * r * (r * s)
    ls = lambda r, t, s, PHI: PHI * r * s

    print(f'nilai volume kerucut adalah\t\t: ', v(r, t, s, PHI))
    print(f'nilai luas permuakaan kerucut adalah\t: ', a(r, t, s, PHI))
    print(f'nilai luas selimut kerucut adalah\t: ', ls(r, t, s, PHI))
kerucut()
print(' -'*30)
kerucut()