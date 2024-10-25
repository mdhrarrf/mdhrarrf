# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Latihan Random 2

while True:
    c = int(input('Masukan suhu dalam celcius:'))

    r = 4/5*c
    f = 9/5*c+32
    k = c+273
    print(f'Reamur: {r}')
    print(f'Fahrenheit: {f}')
    print(f'Kelvin: {k}')

    nilai = int(input('Masukan nilai anda: '))
    if 1 <= nilai <= 50:
        print('Kelompok A')
        if 1 <= nilai <= 25:
            print('A1')
        elif 25 <= nilai <= 50:
            print('A2')

    elif 50 <= nilai <= 100:   
        print('Kelompok B')     
        if 50 <= nilai <= 76:
            print('B1')
        elif 76 <= nilai <= 100:
            print('B2')