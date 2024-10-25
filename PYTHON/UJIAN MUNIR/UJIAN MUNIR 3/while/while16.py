# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping While 16

n = 5
i = 1

while i <= n:
    print(' ' * (n - i) + '*' * (2 * i - 1))
    i += 1

i = 1

while i < n:
    print(' ' * i + '*' * (2 * (n - i) - 1))
    i += 1
