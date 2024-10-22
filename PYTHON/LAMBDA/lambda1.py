sisi = int(input('Sisi\t\t: '))
lebar = int(input('Lebar\t\t: '))

luas = lambda s,l: s * l
keliling = lambda s,l: 4 * s

print('\nLuas\t :', luas(sisi,lebar), 'cm2')
print('Keliling :', keliling(sisi,lebar), 'cm')