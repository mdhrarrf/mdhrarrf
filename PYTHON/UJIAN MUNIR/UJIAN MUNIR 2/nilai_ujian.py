# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Input IF ELSE Nilai

while True:

    nilai = input('\nMasukan nilai: ')

    if nilai >= '80':
        print('\nA')

    elif '70' <= nilai < '80':
        print('\nB')

    elif '55' <= nilai < '70':
        print('\nC')

    elif '40' <= nilai < '55':
        print('\nD')

    elif '0' <= nilai < '40':
        print('\nE')
    
    else:
        print('\nTidak Valid')