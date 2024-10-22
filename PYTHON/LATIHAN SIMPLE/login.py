# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Login

while True:
    print('\n\033[92m==================================')
    print('\033[31m           PROGRAM LOGIN           ')
    print('\033[92m==================================')

    print('\033[37mMasukan Username & Password Anda')

    user = input('\n\033[33mMasukan Username: ')
    pw = input('\033[33mMasukan Password: ')

    true1 = 'admin'
    true2 = 'nimda123'

    if user == true1 and pw == true2:
        print('\n\033[0,31mUsername & Password anda benar :)')
    else:
       print('\n\033[0,35mUsername atau Password anda salah :(')