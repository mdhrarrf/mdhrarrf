# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping While 13

i = 0
star = ''

while i < 5:
    star += '*'
    i += 1
    print(star)

lines = 4
stars = lines

while stars > 0:
    print('*' * stars)
    stars -= 1