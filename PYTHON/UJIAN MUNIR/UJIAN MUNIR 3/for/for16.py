# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping For 16

n = 5

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

for i in range(1, n):
    print(' ' * i + '*' * (2 * (n - i) - 1))