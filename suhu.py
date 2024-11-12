print('=' * 45)
print('\tKonversi Suhu')
print('=' * 45)
celsius = int(input('Masukkan nilai suhu dalam Celsius\t: '))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15
reamur = celsius * 4 / 5

print('Suhu dalam Fahrenheit adalah\t:', fahrenheit, '°F')
print('Suhu dalam Kelvin adalah\t:', kelvin, 'K')
print('Suhu dalam Reamur adalah\t:', reamur, '°R')
