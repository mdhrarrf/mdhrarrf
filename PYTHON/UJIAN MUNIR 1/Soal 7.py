# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Ujian Munir Soal 7

print('=================================')
print('         GEORMETRI TABUNG        ')
print('=================================')

r = input('Masukan jari-jari: ')
t = input('Masukan tinggi   : ')

volume = int(2)*float(3.14)*r*t
luas = float(3.14)*r*r+volume

print(f'\nVolume : {volume}')
print(f'Luas Permukaan : {luas}')