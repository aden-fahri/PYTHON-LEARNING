print("="*50)
print('\tPENENTUAN INDEKS NILAI MAHASISWA')
print("="*50)

nilai_ujian = float(input('Masukkan nilai ujian: '))

if nilai_ujian >= 80:
    indeks_nilai = 'A'
elif 70 <= nilai_ujian < 80:
    indeks_nilai = 'B'
elif 55 <= nilai_ujian < 70:
    indeks_nilai = 'C'
elif 40 <= nilai_ujian < 55:
    indeks_nilai = 'D'
else:
    indeks_nilai = 'E'

print('Nilai ujian \t: ',nilai_ujian)
print('Indeks nilai \t: ',indeks_nilai)