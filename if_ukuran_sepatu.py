print('='*45)
print('\tUkuran Sepatu')
print('='*45)

ukuran_sepatu = int(input("masukkan ukuran sepatu: "))

if ukuran_sepatu > 40 and ukuran_sepatu <= 45:
    print("Ukuran sepatu besar")
elif ukuran_sepatu > 36 and ukuran_sepatu <= 39:
    print("Ukuran sepatu sedang")
elif ukuran_sepatu >= 30 and ukuran_sepatu <= 35:
    print("Ukuran sepatu kecil")
else:
    print("Ukuran salah")
