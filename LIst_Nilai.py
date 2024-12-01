print('='*55)
print('\tMencari Besar Kecil dan Rata-Rata ')
print('='*55)

angka = []
nilai = int(input("Masukkan jumlah nilai\t: "))

for i in range(nilai):
    angka.append(float(input(f'Nilai ke-{i+1}\t\t: ')))

maksimum = max(angka)
minimum = min(angka)
rata_rata = sum(angka) / len(angka)

print('Angka terbesar\t\t: ', maksimum)
print('Angka terkecil\t\t: ', minimum)
print('Rata-rata\t\t: ', rata_rata)
