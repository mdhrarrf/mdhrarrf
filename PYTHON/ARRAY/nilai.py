# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Belajar Array (Nilai)

nilai = []

for i in range(10):
    n = float(input(f"Masukkan nilai ke-{i+1}: "))
    nilai.append(n)

total = max = 0
min = nilai[0]

for data in nilai:
    total += data

    if data > max:
        max = data

    if data < min:
        min = data

print(f'\nJumlah : {total}')
print(f'Rata-rata : {total/n}')
print(f'Nilai Terbesar : {max}')
print(f'Nilai Terkecil : {min}')
