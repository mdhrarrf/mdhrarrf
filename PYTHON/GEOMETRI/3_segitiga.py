# Muhammad Haidar Almer Rafif
# 24/09/24
# Program Geometri Segitiga

def segitiga():
    a = int(input('\nMasukan Alas Segitiga: '))
    t = int(input('Masukan Tinggi Segitiga: '))
    s1 = int(input('Masukan Sisi 1 Segitiga: '))
    s2 = int(input('Masukan Sisi 2 Segitiga: '))
    s3 = int(input('Masukan Sisi 3 Segitiga: '))

    l = lambda a,t: 0.5*a*t
    k = lambda s1,s2,s3: s1+s2+s3

    print(f'\nLuas Segitiga = {round (l(a,t),2)} cm2')
    print(f'Keliling Segitiga = {round (k(s1,s2,s3),2)} cm')
segitiga()