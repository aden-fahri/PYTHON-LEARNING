print('='*45)
print('\tHURUF VOKAL DAN KONSONAN')
print('='*45)

huruf = (input("Masukkan 1 huruf : ")).upper()

vokal = ['A','I','U','E','O']

if huruf in vokal:
     print (f'{huruf} adalah huruf Vokal')
else:
     print (f'{huruf} adalah huruf Konsonan')