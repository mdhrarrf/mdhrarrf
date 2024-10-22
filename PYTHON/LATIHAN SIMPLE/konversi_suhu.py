# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Konversi Suhu

print('=============================')
print('    PROGRAM KONVERSI SUHU    ')
print('=============================')
while True:
    celcius = input('Masukan suhu (dalam celcius): ')
    fahren = int(celcius)*float(1.8)+int(32)
    reamur = float(0.8)*int(celcius)
    print(f'Suhu dalam Fahrenheit: {round (fahren, 2)}')
    print(f'Suhu dalam Reamur: {round (reamur,2)}')