print('='*50)
print('\t\tMengurutkan angka')
print('='*50)

v = int(input('Masukkan angka : '))
w = int(input('Masukkan angka : '))
x = int(input('Masukkan angka : '))
y = int(input('Masukkan angka : '))
z = int(input('Masukkan angka : '))

urutan = [v, w, x, y, z]

urutan.sort()

print('Angka terbesar adalah:',urutan)
print('Angka terkecil adalah:', urutan[0])