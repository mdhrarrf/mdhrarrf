# Muhammad Haidar Almer Rafif
# 08/10/24
# Program Geometri Trapesium

def trapesium():
    a = int(input('\nMasukan Sisi Sejajar Pertama\t: '))
    b = int(input('Masukan Sisi Sejajar Kedua\t: '))
    c = int(input('Masukan Sisi Sejajar Ketiga\t: '))
    d = int(input('Masukan Sisi Sejajar Keempat\t: '))
    t = int(input('Masukan Tinggi\t\t\t: '))

    l = lambda a,b,t: a + b * 0.5 * t
    k = lambda a,b,c,d: a + b + c + d
    
    print('\nLuas\t\t\t:', (round(l(a,b,t),2)), 'cm2')
    print('Keliling\t\t:', (round(k(a,b,c,d),2)), 'cm')
trapesium()