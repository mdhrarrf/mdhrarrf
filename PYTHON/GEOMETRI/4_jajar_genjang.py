# Muhammad Haidar Almer Rafif
# 08/10/24
# Program Geometri Jajar Genjang

def jajar_genjang():
    a = int(input('\nMasukan Sisi Pertama\t: '))
    b = int(input('Masukan Sisi Kedua\t: '))
    t = int(input('Masukan Tinggi\t\t: '))

    l = lambda a,t: a * t
    k = lambda a,b: a + b * 2
    
    print('\nLuas\t\t\t:', (round(l(a,t),2)), 'cm2')
    print('Keliling\t\t:', (round(k(a,b),2)), 'cm')
jajar_genjang()