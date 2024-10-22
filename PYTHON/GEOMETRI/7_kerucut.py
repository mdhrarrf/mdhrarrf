# Muhammad Haidar Almer Rafif
# 08/10/24
# Program Geometri Kerucut

def kerucut():
    r = int(input('\nMasukan Jari-jari\t: '))
    h = int(input('Masukan Tinggi\t\t: '))
    s = int(input('Masukan Panjang Garis Miring : '))

    phi = 3.14
    v = lambda phi,r,h: 0.33333333333 * phi * r * r * h
    a = lambda r,s,phi: r + s * phi * r
    
    print('\nVolume\t\t\t:', (round(v(phi,r,h),2)), 'cm3')
    print('Luas Permukaan\t\t:', (round(a(r,s,phi),2)), 'cm2')
kerucut()