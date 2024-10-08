# Muhammad Haidar Almer Rafif
# 08/10/24
# Program Geometri Balok

def balok():
    p = int(input('\nMasukan Panjang\t\t: '))
    t = int(input('Masukan Tinggi\t\t: '))
    l = int(input('Masukan Lebar\t\t: '))

    v = lambda p,l,t: p * l * t
    a = lambda p,l,t: p * l + p * t + l * t * 2
    
    print('\nVolume\t\t\t:', (round(v(p,l,t),2)), 'cm3')
    print('Luas Permukaan\t\t:', (round(a(p,l,t),2)), 'cm2')
balok()