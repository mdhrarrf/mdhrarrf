# Muhammad Haidar Almer Rafif
# 24/09/24
# Program Geometri Persegi

def persegi():
    s = int(input('\nMasukan Sisi Persegi: '))

    l = lambda s: s*s
    k = lambda s: 4*s

    print(f'\nLuas Persegi : {round (l(s),2)} cm2')
    print(f'Keliling Persegi : {round (k(s),2)} cm')
persegi()