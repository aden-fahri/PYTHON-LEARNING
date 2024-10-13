print('='*30)
print('nilai siswa')
print('='*30)

nilai = int(input('masukkan nilai siswa: '))

if nilai >= 90 and nilai <= 100:
    print('Nilai A')
elif nilai >= 80 and nilai <= 89:
    print('Nilai B')
elif nilai >= 70 and nilai <= 79:
    print('Nilai C')
elif nilai >= 60 and nilai <= 69:
    print('Nilai E')
else:
    nilai <= 60
    print('Nilai E')

