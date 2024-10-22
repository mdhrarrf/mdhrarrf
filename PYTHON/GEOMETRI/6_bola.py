# Muhammad Haidar Almer Rafif
# 08/10/24
# Program Geometri Bola

def bola():
    r = int(input('\nMasukan Jari-jari\t: '))

    phi = 3.14
    v = lambda r,phi: phi * r * r * r * 1.33333333333
    a = lambda phi,r: 4 * phi * r * r
    
    print('\nVolume\t\t\t:', (round(v(r,phi),2)), 'cm3')
    print('Luas Permukaan\t\t:', (round(a(phi,r),2)), 'cm2')
bola()