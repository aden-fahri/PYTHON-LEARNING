print('='*60)
print('\t\tANGKA JEPANG (KANJI)')
print('='*60)

angka = int(input('Masukkan angka 1-10 \t\t\t: '))

angka_jepang_kanji= ['一 (ICHI)', '二 (NI)', '三 (SAN)', '四 (YON/SHI)', '五 (GO)', '六 (ROKU)', '七 (NANA/SHICHI)', '八 (HACHI)', '九 (KYUU)', '十 (JUU)']

if 1 <=  angka <= 10:
    print(f"{angka} dalam angka jepang (kanji) adalah\t: {angka_jepang_kanji[angka-1]}")
else:
    print('Angka salah. Tolong masukkan angka 1-10.')