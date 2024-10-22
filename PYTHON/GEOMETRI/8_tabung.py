# Muhammad Haidar Almer Rafif
# 08/10/24
# Program Geometri Tabung

def tabung():
    r = int(input('\nMasukan Jari-jari\t: '))
    h = int(input('Masukan Tinggi\t\t: '))

    phi = 3.14
    v = lambda phi,r,h: phi * r * r * h
    a = lambda r,h,phi: r + h * 2 * phi * r
    
    print('\nVolume\t\t\t:', (round(v(phi,r,h),2)), 'cm3')
    print('Luas Permukaan\t\t:', (round(a(r,h,phi),2)), 'cm2')
tabung()