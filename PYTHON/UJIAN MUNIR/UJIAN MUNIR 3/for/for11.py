# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping For 11

i = 0
star = ''

while i < 4:
    star += '*'
    i += 1
    print(star)

i = 1

while i < 3:
    print('*',end='')
    i += 1

lines = 5
stars = lines

while stars > 0:
    print('*' * stars)
    stars -= 1