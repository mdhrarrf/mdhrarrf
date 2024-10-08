# Muhammad Haidar Almer Rafif
# 24/09/24
# Program Geometri Lingkaran

def lingkaran():
    r = int(input('\nMasukan Jari jari lingkaran: '))

    phi = 3.14
    k = lambda r,phi: 2*phi*r
    l = lambda r,phi: phi*r*r

    print('\nKeliling Lingkaran =', (round (k(r,phi),2)), 'cm')
    print('Luas Lingkaran =', (round (l(r,phi),2)),'cm2')
lingkaran()