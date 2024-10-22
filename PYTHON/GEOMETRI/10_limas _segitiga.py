# Muhammad Haidar Almer Rafif
# 08/10/24
# Program Geometri Limas Segitiga

def limas_segitiga():
    s = int(input('\nMasukan Panjang Garis Miring\t: '))
    t = int(input('Masukan Tinggi\t\t\t: '))
    l = int(input('Masukan Luas Alas\t\t: '))
    p = int(input('Masukan Keliling Alas\t\t: '))
    

    v = lambda l,t: 0.33333333333 * l * t
    a = lambda l,p,s: l + 0.33333333333 * p * s
    
    print('\nVolume\t\t\t:', (round(v(l,t),2)), 'cm3')
    print('Luas Permukaan\t\t:', (round(a(l,p,s),2)), 'cm2')
limas_segitiga()